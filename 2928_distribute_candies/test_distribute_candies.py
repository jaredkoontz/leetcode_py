# https://leetcode.com/problems/distribute-candies-among-children-i
from functools import cache

import pytest


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return self.distributeCandies_dfs(n, limit)

    @staticmethod
    def distributeCandies_dfs(n: int, limit: int) -> int:
        @cache
        def dist(i, left):
            if i == 3:
                if left == 0:
                    return 1
                return 0
            res = 0
            for num in range(min(left, limit) + 1):
                res += dist(i + 1, left - num)
            return res

        return dist(0, n)

    @staticmethod
    def distributeCandies_math(n: int, limit: int) -> int:
        if n > 3 * limit:
            return 0
        res = (n + 2) * (n + 1) // 2
        if n > limit:
            res -= 3 * (n - limit + 1) * (n - limit) // 2
        if n - 2 >= 2 * limit:
            res += 3 * (n - 2 * limit) * (n - 2 * limit - 1) // 2
        return res

    @staticmethod
    def distributeCandies_naive(n: int, limit: int) -> int:
        num_ways = 0
        for first_child in range(limit + 1):
            for second_child in range(limit + 1):
                for third_child in range(limit + 1):
                    candies_given = first_child + second_child + third_child
                    if candies_given == n:
                        num_ways += 1
        return num_ways


@pytest.mark.parametrize(
    "l1,limit,output",
    [
        (5, 2, 3),
        (3, 3, 10),
        (3, 2, 7),
        (2, 2, 6),
    ],
)
def test_distribute_candies(l1, limit, output):
    assert Solution().distributeCandies(l1, limit) == output
