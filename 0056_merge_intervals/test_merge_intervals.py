import pytest


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        return self.merge_mine(intervals)

    @staticmethod
    def merge_mine(intervals: list[list[int]]) -> list[list[int]]:
        merged_intervals = []
        for candidate in sorted(intervals, key=lambda start: start[0]):
            start_of_interval = 0
            end_of_interval = 1
            last_interval = merged_intervals[-1] if merged_intervals else []
            if (
                merged_intervals
                and candidate[start_of_interval] <= last_interval[end_of_interval]
            ):
                last_interval[1] = max(
                    last_interval[end_of_interval], candidate[end_of_interval]
                )
            else:
                merged_intervals += [candidate]
        return merged_intervals


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
    ],
)
def test_merge(intervals, expected):
    assert Solution().merge(intervals) == expected
