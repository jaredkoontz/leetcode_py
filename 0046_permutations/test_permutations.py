# https://leetcode.com/problems/permutations
from collections import deque

import pytest


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return self.permute_backtrack(nums)

    @staticmethod
    def permute_backtrack(nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans, sol = [], []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()

        backtrack()
        return ans

    @staticmethod
    def permute_no_backtrack(nums: list[int]) -> list[list[int]]:
        def recursive(all_nums, perm=None, res=None):
            if res is None:
                res = []
            if perm is None:
                perm = []
            if not all_nums:
                res.append(
                    perm
                )  # --- no need to copy as we are not popping/backtracking. Instead we're passing a new variable each time

            for i in range(len(all_nums)):
                new_nums = all_nums[:i] + all_nums[i + 1 :]
                # perm.append(nums[i]) # --- instead of appending to the same variable
                new_perm = perm + [all_nums[i]]  # --- new copy of the data/variable
                recursive(new_nums, new_perm, res)
                # perm.pop()  # --- no need to backtrack
            return res

        return recursive(nums)

    @staticmethod
    def permute_dfs(nums: list[int]) -> list[list[int]]:
        stack = [(nums, [])]  # -- nums, path (or perms)
        res = []
        while stack:
            nums, path = stack.pop()
            if not nums:
                res.append(path)
            for i in range(len(nums)):  # -- NOTE [4]
                new_nums = nums[:i] + nums[i + 1 :]
                stack.append(
                    (new_nums, path + [nums[i]])
                )  # --  just like we used to do (path + [node.val]) in tree traversal
        return res

    @staticmethod
    def permute_bfs(nums: list[int]) -> list[list[int]]:
        q = deque()
        q.append((nums, []))  # -- nums, path (or perms)
        res = []
        while q:
            nums, path = q.popleft()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                new_nums = nums[:i] + nums[i + 1 :]
                q.append((new_nums, path + [nums[i]]))
        return res


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ],
)
def test_permute(nums, expected):
    assert Solution().permute(nums) == expected
