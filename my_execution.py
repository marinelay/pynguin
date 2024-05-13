import argparse
import dataclasses
import os
import sys
import xml.etree.ElementTree as ET
import subprocess
from pathlib import Path
from typing import List, Union, Tuple, Dict, Optional
import subprocess

@dataclasses.dataclass
class SLURMSetup:
    iterations: int
    constraint: str
    docker_images: Dict[str, Tuple[Union[str, os.PathLike], str]]


@dataclasses.dataclass
class Project:
    name: str
    version: str
    sources: Union[str, os.PathLike]
    modules: List[str]


@dataclasses.dataclass
class Run:
    constraint: str
    docker_images: Dict[str, Tuple[Union[str, os.PathLike], str]]
    configuration_name: str
    configuration_options: List[str]
    project_name: str
    project_version: str
    project_sources: Union[str, os.PathLike]
    module: str
    iteration: int
    run_id: int


def _parse_xml(
        file_name: Union[str, os.PathLike]
) -> Tuple[SLURMSetup, Dict[str, List[str]], List[Project]]:
    tree = ET.ElementTree(file=file_name)
    experiment = tree.getroot()
    slurm_setup = _get_slurm_setup(experiment)

    setup = experiment.find("setup")
    configurations = setup.find("configurations")
    global_config = _get_global_config(configurations.find("global"))
    configs: Dict[str, List[str]] = {}
    for configuration in configurations.findall("configuration"):
        name, values = _get_configuration(configuration)
        configs[name] = values

    # output_variables: List[str] = []
    # for output_variable in setup.find("output-variables").findall("output-variable"):
    #     output_variables.append(output_variable.text)
    # output_vars = "--output_variables " + ",".join(output_variables)
    # global_config.append(output_vars)

    run_configurations: Dict[str, List[str]] = {}
    for config_name, configuration in configs.items():
        run_configurations[config_name] = global_config + configuration

    project_tags = experiment.find("projects")
    projects: List[Project] = []
    for project in project_tags.findall("project"):
        projects.append(_get_project(project))

    return slurm_setup, run_configurations, projects

def _get_slurm_setup(experiment: ET.Element) -> SLURMSetup:
    iterations = experiment.attrib["iterations"]
    setup = experiment.find("setup")
    constraint = setup.find("constraint").text
    docker_images: Dict[str, Tuple[Union[str, os.PathLike], str]] = {}
    for docker in setup.findall("docker"):
        docker_images[docker.attrib["name"]] = (
            docker.attrib["path"], docker.attrib["version"]
        )
    return SLURMSetup(
        iterations=int(iterations),
        constraint=constraint,
        docker_images=docker_images,
    )


def _get_global_config(element: Optional[ET.Element]) -> List[str]:
    if element is None:
        return []
    result = []
    for option in element:
        result.append(
            f'--{option.attrib["key"]} {option.attrib["value"]}'
        )
    return result


def _get_configuration(configuration: ET.Element) -> Tuple[str, List[str]]:
    name = configuration.attrib["id"]
    values: List[str] = []
    for option in configuration.findall("option"):
        values.append(
            f'--{option.attrib["key"]} {option.attrib["value"]}'
        )
    return name, values


def _get_project(project: ET.Element) -> Project:
    name = project.find("name").text
    version = project.find("version").text
    sources = project.find("sources").text
    modules: List[str] = []
    for module in project.find("modules").findall("module"):
        modules.append(module.text)
    return Project(
        name=name,
        version=version,
        sources=sources,
        modules=modules,
    )

def main(argv: List[str]) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--definition",
        dest="definition",
        required=True,
        help="Path to run-definition XML file.",
    )
    config = parser.parse_args(argv[1:])
    slurm_setup, run_configurations, projects = _parse_xml(config.definition)
    
    for name, configuration in run_configurations.items() :
        for project in projects :
            sources = project.sources
            modules = project.modules
            for module in modules :
                configuration.append("--project-path " + sources)
                configuration.append("--module-name " + module)
                configuration.append("--output-path " + sources + "/testgen")
                configuration.append("--report-dir " + sources + "/coverage-report")
                # configuration.append("-v")

                print("Start", module)

                command = " ".join(["pynguin"] + configuration)
                result = subprocess.run(command, shell=True, capture_output=True)

                if result.returncode == 0 :
                    print("End with", result.returncode)
                else :
                    with open(module+'.log', 'w+') as f :
                        f.write(result.stderr.decode('utf-8'))
                    print("End with", result.returncode)

if __name__ == '__main__':
    main(sys.argv)
