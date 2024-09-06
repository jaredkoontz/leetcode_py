# https://leetcode.com/problems/combination-sum
import pytest

from helpers.testing_helpers import freeze_nested_lists


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        return self.combinationSum_backtrack(candidates, target)

    @staticmethod
    def combinationSum_backtrack(candidates: list[int], target: int) -> list[list[int]]:
        ret = []

        def dfs(i: int, current: list[int], total: int):
            if total == target:
                ret.append(current[:])
                return
            if i >= len(candidates) or total > target:
                return

            current.append(candidates[i])
            dfs(i, current, total + candidates[i])
            current.pop()
            dfs(i + 1, current, total)
            return

        dfs(0, [], 0)
        return ret


@pytest.mark.parametrize(
    "candidates,target,expected",
    [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    ],
)
def test_combinationSum2(candidates, target, expected):
    frozen1, frozen2 = freeze_nested_lists(
        Solution().combinationSum(candidates, target), expected
    )
    assert frozen1 == frozen2
