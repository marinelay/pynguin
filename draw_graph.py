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
    # "queue1",
    "queue2",
    "queue3",
    "queue4",
    "queue5",
    "sort1",
    "stack1",
    # "stack2",
    "stack3",
    "stack4",
    # "stack5"
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
    bench_path = Path("python_experiments")

    fig, axs = plt.subplots(3, 6, figsize=(20, 10))

    for i, name in enumerate(project):
        coverage_report_path = bench_path / name / "coverage-report"

        with open(coverage_report_path / "time-coverage.json", "r") as file:
            time_coverage = json.load(file)

        baseline = time_coverage[:3]
        my_execution = time_coverage[3:9]
        re_baseline = time_coverage[9:]

        try:
            draw_coverage_graph(axs[i // 6, i % 6], baseline + re_baseline, label="Baseline")
            draw_coverage_graph(axs[i // 6, i % 6], my_execution, label="Ours")
        except:
            print(name)
            continue

        axs[i // 6, i % 6].set_xlabel('Time')
        axs[i // 6, i % 6].set_ylabel('Average Coverage')
        axs[i // 6, i % 6].set_title(name)
        axs[i // 6, i % 6].grid(True)
        axs[i // 6, i % 6].legend()

    # 각 subplot의 범례를 숨김
    for ax in axs:
        for a in ax:
            a.legend().set_visible(False)

    handles, labels = axs[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower left', ncol=2)

    plt.tight_layout()
    plt.savefig("merged_time_coverage_subplot.png")
    plt.clf()

if __name__ == '__main__':
    main(sys.argv)
