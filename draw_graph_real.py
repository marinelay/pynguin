import argparse
import dataclasses
import os
import sys
import xml.etree.ElementTree as ET
import subprocess
from pathlib import Path
from typing import List, Union, Tuple, Dict, Optional
import subprocess
import matplotlib.pyplot as plt
import json
import numpy as np

project = [
    "thonny",
    "sanic",
    "codetiming",
]

project_name = [
    "thonny/roughparse.py",
    "sanic/cookies.py",
    "codetiming/_time.py"
]

def draw_coverage_graph(ax, time_coverages, label) -> None:
    all_times = sorted(set([time for dataset in time_coverages for time, _ in dataset]))
    min_time = min(all_times)
    max_time = max(all_times)
    common_times = np.linspace(min_time, max_time, num=100)

    interpolated_data = []
    for dataset in time_coverages:
        times, coverages = zip(*dataset)
        interpolated_coverages = np.interp(common_times, times, coverages, left=coverages[0], right=coverages[-1])
        interpolated_data.append(interpolated_coverages)

        # print(interpolated_coverages)

    # 시간별 평균 커버리지 계산
    average_coverages = np.mean(interpolated_data, axis=0)

    # 그래프 그리기
    ax.plot(common_times, average_coverages, marker='o', linewidth=0.5, markersize=1, label=label)
    



def main(argv: List[str]) -> None:
    bench_path = Path("projects")

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    for i, name in enumerate(project):
        coverage_report_path = bench_path / name / "coverage_report"

        with open(coverage_report_path / "time-coverage.json", "r") as file:
            time_coverage = json.load(file)

        middle = len(time_coverage) // 2
        print(name, middle)

        baseline = time_coverage[:middle]
        my_execution = time_coverage[middle:]

        try:
            draw_coverage_graph(axs[i], baseline, label="Baseline")
            draw_coverage_graph(axs[i], my_execution, label="Ours")
        except:
            print(name)
            continue

        axs[i].set_xlabel('Time')
        axs[i].set_ylabel('Average Coverage')
        axs[i].set_title(project_name[i])
        axs[i].grid(True)
        axs[i].legend()

    # 각 subplot의 범례를 숨김
    for ax in axs:
        ax.legend().set_visible(False)

    handles, labels = axs[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower left', ncol=2)

    plt.tight_layout()
    plt.savefig("merged_time_coverage_real.png")
    plt.clf()

if __name__ == '__main__':
    main(sys.argv)
