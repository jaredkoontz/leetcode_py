import pytest


class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        return self.maxDistance_mine(arrays)

    @staticmethod
    def maxDistance_mine(arrays: list[list[int]]) -> int:
        curr_min = arrays[0][0]
        curr_max = arrays[0][-1]
        curr_sum = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            # calculating the sum first is why we don't use two from the same arr
            local_sum = max((arr[-1] - curr_min), (curr_max - arr[0]))
            curr_sum = max(curr_sum, local_sum)

            curr_min = min(curr_min, arr[0])
            curr_max = max(curr_max, arr[-1])
        return curr_sum


@pytest.mark.parametrize(
    "arrays,expected",
    [
        ([[1, 4], [0, 5]], 4),
        ([[2, 2], [1, 5], [0, 6]], 5),
        ([[1, 2, 3], [4, 5], [1, 2, 3]], 4),
        ([[1], [1]], 0),
    ],
)
def test_maxDistance(arrays, expected):
    assert Solution().maxDistance(arrays) == expected
