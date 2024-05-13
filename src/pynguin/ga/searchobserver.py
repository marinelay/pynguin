#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2024 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT

#  This file is part of Pynguin.
#
#
#  SPDX-License-Identifier: MIT
#
"""Provides an observer to observe the search."""
from __future__ import annotations

import logging

from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING

import time
import pynguin.configuration as config
from pathlib import Path
import json
import os

if TYPE_CHECKING:
    import pynguin.ga.testsuitechromosome as tsc


class SearchObserver(ABC):
    """Observes the execution of a search algorithm."""

    @abstractmethod
    def before_search_start(self, start_time_ns: int) -> None:
        """Called when the search starts.

        Args:
            start_time_ns: time since epoch in ns when the search started.
        """

    # TODO(fk) Unsure about API here, I mean we always produce a suite.

    @abstractmethod
    def before_first_search_iteration(self, initial: tsc.TestSuiteChromosome) -> None:
        """Called once before the very first iteration of the search algorithm.

        Calling this is optional, as not every approach has a result before
        the first iteration.

        Args:
            initial: The initially produced test suite.
        """

    @abstractmethod
    def after_search_iteration(self, best: tsc.TestSuiteChromosome) -> None:
        """Called after every iteration of the search algorithm.

        Args:
            best: The currently best produced test suite.
        """

    @abstractmethod
    def after_search_finish(self) -> None:
        """Called when the search has finished."""


class LogSearchObserver(SearchObserver):
    """Observes the search and creates some log output."""

    _logger = logging.getLogger(__name__)

    def __init__(self):  # noqa: D107
        self.start_time = time.monotonic()
        self.iteration = 0
        self.cur_best_cov = 0
        self.cov_log = [] # (time, cov)

    def before_search_start(self, start_time_ns: int) -> None:  # noqa: D102
        self.iteration = 0

    def before_first_search_iteration(  # noqa: D102
        self, initial: tsc.TestSuiteChromosome
    ) -> None:
        self._logger.info("Initial Population, Coverage: %5f", initial.get_coverage())

    def after_search_iteration(  # noqa: D102
        self, best: tsc.TestSuiteChromosome
    ) -> None:
        self.iteration += 1
        if best.get_coverage() > self.cur_best_cov:
            self.cur_best_cov = best.get_coverage()
            self.cov_log.append((round(time.monotonic() - self.start_time, 2), round(self.cur_best_cov, 2)))
        self._logger.info(
            "Time: %8.2f, Iteration: %7i, Coverage: %5f", time.monotonic() - self.start_time, self.iteration, best.get_coverage()
        )

    def after_search_finish(self) -> None:
        self._logger.info(f"{self.cov_log}")
        report_dir = Path(config.configuration.statistics_output.report_dir).absolute()

        # 파일이 존재하는지 확인
        if os.path.exists(report_dir / "time-coverage.json"):
            # 파일이 존재할 경우, 파일 열어서 데이터 읽기
            with open(report_dir / "time-coverage.json", 'r') as file:
                data = json.load(file)
        else:
            # 파일이 존재하지 않을 경우, 빈 데이터 생성
            data = []

        data.append(self.cov_log)

        with open(report_dir / "time-coverage.json", "w") as f:
            json.dump(data, f, indent=4)
        """Not used."""
