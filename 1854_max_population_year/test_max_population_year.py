# https://leetcode.com/problems/maximum-population-year
from collections import defaultdict

import pytest


class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        return self.maximumPopulation_mine(logs)

    @staticmethod
    def maximumPopulation_mine(logs: list[list[int]]) -> int:
        year_changes = defaultdict(int)

        for birth, death in logs:
            year_changes[birth] += 1
            year_changes[death] -= 1

        max_population = 0
        current_population = 0
        ans_year = None

        for year in sorted(year_changes):
            current_population += year_changes[year]
            if current_population > max_population:
                max_population = current_population
                ans_year = year

        return ans_year

    @staticmethod
    def maximumPopulation_theirs(logs: list[list[int]]) -> int:
        dates = []
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))

        dates.sort()

        population = max_population = max_year = 0
        for year, change in dates:
            population += change
            if population > max_population:
                max_population = population
                max_year = year

        return max_year


@pytest.mark.parametrize(
    "logs,expected",
    [
        ([[1993, 1999], [2000, 2010]], 1993),
        ([[1950, 1961], [1960, 1971], [1970, 1981]], 1960),
    ],
)
def test_maximumPopulation(logs, expected):
    assert Solution().maximumPopulation(logs) == expected
