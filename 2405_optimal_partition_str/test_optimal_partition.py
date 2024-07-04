import pytest


class Solution:
    def partitionString(self, s: str) -> int:
        return self.partitionString_mine(s)

    @staticmethod
    def partitionString_mine(s: str) -> int:
        if not s:
            return 0
        num_ways = 0
        curr_set = set()
        for ch in s:
            if ch in curr_set:
                num_ways += 1
                curr_set.clear()
            curr_set.add(ch)
        return num_ways + 1 if curr_set else num_ways


@pytest.mark.parametrize(
    "s,expected",
    [
        ("abacaba", 4),
        ("ssssss", 6),
    ],
)
def test_optimal_partition(s, expected):
    assert Solution().partitionString(s) == expected
