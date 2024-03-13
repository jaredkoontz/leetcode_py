from math import sqrt

import pytest


class Solution:
    def pivotInteger(self, n: int) -> int:
        return self.pivotInteger_theirs2(n)

    def pivotInteger_theirs2(self, n: int) -> int:
        if n < 1:
            return -1
        x = sqrt(n * (n + 1) / 2)

        if x % 1 != 0:
            return -1
        else:
            return int(x)

    def pivotInteger_theirs(self, n: int) -> int:
        for i in range(1, n + 1):
            # Calculate the sum of elements from 1 to i using arithmetic progression formula
            left_sum = i * (i + 1) // 2
            # Calculate the sum of elements from i to n using arithmetic progression formula
            right_sum = n * (n + 1) // 2 - i * (i - 1) // 2
            if left_sum == right_sum:
                return i  # Return i as the pivot integer
        return -1  # If no such integer exists, return -1

    def pivotInteger_mine(self, n: int) -> int:
        for i in range(1, n + 1):
            left_sum, right_sum = self.find_sums(i, n)
            if left_sum == right_sum:
                return i
        return -1

    def find_sums(self, i, n):
        left_sum = 0
        right_sum = 0
        for i in range(1, i + 1):
            left_sum += i
        for i in range(i, n + 1):
            right_sum += i
        return left_sum, right_sum


@pytest.mark.parametrize(
    "x, n",
    [
        (8, 6),
        (1, 1),
        (4, -1),
        (5, -1),
        (0, -1),
    ],
)
def test_pivotInteger(x, n):
    assert Solution().pivotInteger(x) == n
