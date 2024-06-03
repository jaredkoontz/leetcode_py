import pytest


class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        res = cur = 0
        count = {0: [1, 0]}
        for i, a in enumerate(arr):
            cur ^= a
            n, total = count.get(cur, [0, 0])
            res += i * n - total
            count[cur] = [n + 1, total + i + 1]
        return res


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([2, 3, 1, 6, 7], 4),
        ([1, 1, 1, 1, 1], 10),
    ],
)
def test_countTriplets(arr, expected):
    assert Solution().countTriplets(arr) == expected
