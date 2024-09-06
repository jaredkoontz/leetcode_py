# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk
import pytest


class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        return self.chalkReplacer_prefix_sum(chalk, k)

    @staticmethod
    def chalkReplacer_readable(chalk: list[int], k: int) -> int:
        s = sum(chalk)

        k = k % s

        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]

        return len(chalk) - 1

    @staticmethod
    def chalkReplacer_bin_search(chalk: list[int], k: int) -> int:
        def __binary_search(arr, tar):
            low = 0
            high = len(arr) - 1

            while low < high:
                mid = low + (high - low) // 2

                if arr[mid] <= tar:
                    low = mid + 1
                else:
                    high = mid

            return high

        n = len(chalk)

        prefix_sum = [0] * n
        prefix_sum[0] = chalk[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + chalk[i]

        sum_chalk = prefix_sum[n - 1]
        remaining_chalk = k % sum_chalk

        return __binary_search(prefix_sum, remaining_chalk)

    @staticmethod
    def chalkReplacer_prefix_sum(chalk: list[int], k: int) -> int:
        # Find the sum of all elements.
        sum_chalk = 0
        for i in range(len(chalk)):
            sum_chalk += chalk[i]
            if sum_chalk > k:
                break
        # Find modulo of k with sum.
        k = k % sum_chalk
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
        return 0

    @staticmethod
    def chalkReplacer_naive(chalk: list[int], k: int) -> int:
        i = 0
        while True:
            if chalk[i] > k:
                break
            k -= chalk[i]
            i += 1
            i %= len(chalk)
        return i


@pytest.mark.parametrize(
    "chalk,k,expected",
    [
        ([5, 1, 5], 22, 0),
        ([6, 1, 5], 5, 0),
        ([3, 4, 1, 2], 25, 1),
    ],
)
def test_chalkReplacer(chalk, k, expected):
    assert Solution().chalkReplacer(chalk, k) == expected
