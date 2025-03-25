# https://leetcode.com/problems/unique-binary-search-trees
import functools

import pytest


class Solution:
    def numTrees(self, n: int) -> int:
        return self.numTrees_best(n)

    @staticmethod
    def numTrees_best(n: int) -> int:
        counts = {}

        def countTrees(start, end):
            if start > end:
                return 1
            if (start, end) in counts:
                return counts[(start, end)]
            count = 0
            for i in range(start, end + 1):
                left_count = countTrees(start, i - 1)
                right_count = countTrees(i + 1, end)
                count += left_count * right_count
            counts[(start, end)] = count
            return count

        return countTrees(1, n)

    @staticmethod
    def numTrees_catalan(n: int) -> int:
        catalan_number = 1
        for index in range(1, n + 1):
            catalan_number = catalan_number * 2 * (2 * index - 1) / (index + 1)
        return int(catalan_number)

    @staticmethod
    def numTrees_memo(n: int) -> int:
        def helper(start, end):
            if start >= end:
                return 1  # empty or single node tree is 1 unique BST

            distance = end - start
            if memo[distance + 1] == 0:
                total = 0
                for root in range(start, end + 1):
                    left_trees = helper(start, root - 1)
                    right_trees = helper(root + 1, end)
                    total += left_trees * right_trees
                memo[distance + 1] = total
            return memo[distance + 1]

        memo = [0] * (max(n, 4) + 1)
        memo[0] = 1
        memo[1] = 1
        memo[2] = 2
        memo[3] = 5
        if memo[n] != 0:
            return memo[n]
        return helper(1, n)

    @staticmethod
    def numTrees_cache(n: int) -> int:
        @functools.cache
        def helper(start, end):
            if start >= end:
                return 1  # empty or single node tree is 1 unique BST

            total = 0
            for root in range(start, end + 1):
                left_trees = helper(start, root - 1)
                right_trees = helper(root + 1, end)
                total += left_trees * right_trees
            return total

        return helper(1, n)

    @staticmethod
    def numTrees_naive(n: int) -> int:
        def helper(start, end):
            if start >= end:
                return 1  # empty or single node tree is 1 unique BST

            total = 0
            for root in range(start, end + 1):
                left_trees = helper(start, root - 1)
                right_trees = helper(root + 1, end)
                total += left_trees * right_trees
            return total

        return helper(1, n)


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 5),
        (4, 14),
        (5, 42),
        (6, 132),
        (7, 429),
        (35, 3_116_285_494_907_301_262),
    ],
)
def test_numTrees(n, expected):
    assert Solution().numTrees(n) == expected
