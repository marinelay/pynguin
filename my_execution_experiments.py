import argparse
import dataclasses
import os
import sys
import xml.etree.ElementTree as ET
import subprocess
from pathlib import Path
from typing import List, Union, Tuple, Dict, Optional
import subprocess

project = [
    "binarySearchTree1",
    "binarySearchTree2",
    "binarySearchTree3",
    "binarySearchTree4",
    "identifier1",
    "linkedList1",
    "linkedList2",
    "linkedList3",
    "linkedList4",
    "linkedList5",
    "queue1",
    "queue2",
    "queue3",
    "queue4",
    "queue5",
    "sort1",
    "stack1",
    "stack2",
    "stack3",
    "stack4",
    "stack5"
]

def main(argv: List[str]) -> None:
    parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "-d",
    #     "--definition",
    #     dest="definition",
    #     required=True,
    #     help="Path to run-definition XML file.",
    # )
    # config = parser.parse_args(argv[1:])
    # slurm_setup, run_configurations, projects = _parse_xml(config.definition)
    
    bench_path = Path("python_experiments")

    for name in project :
        for i in range(3):
            sources = str(bench_path / name)
            module = name

            configuration = [
                "--maximum-search-time 300",
                "--assertion-generation NONE",
                "--type_inference_strategy TYPE_HINTS"
            ]

            configuration.append("--project-path " + sources)
            configuration.append("--module-name " + module)
            configuration.append("--output-path " + sources + "/testgen")
            configuration.append("--report-dir " + sources + "/coverage-report")
            # configuration.append("-v")

            print("Start", module, i)

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
