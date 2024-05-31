import pytest

from helpers.test_helpers import compare_nested_lists


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # assert (
        #     self.subsets_iterative(nums)
        #     == self.subsets_bit(nums)
        #     == self.subsets_dfs(nums)
        #     == self.subsets_backtrack(nums)
        # )
        return self.subsets_backtrack(nums)

    @staticmethod
    def subsets_iterative(nums: list[int]) -> list[list[int]]:
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res
        pass

    @staticmethod
    def subsets_bit(nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res

    @staticmethod
    def subsets_dfs(nums: list[int]) -> list[list[int]]:
        def dfs(nums, path, ret):
            ret.append(path)
            for i in range(len(nums)):
                dfs(nums[i + 1 :], path + [nums[i]], ret)

        ret = []
        dfs(nums, [], ret)
        return ret

    @staticmethod
    def subsets_backtrack(nums: list[int]) -> list[list[int]]:
        sol = []
        ret = []
        n = len(nums)

        def backtrack(i=0):
            if i == n:
                ret.append(sol[:])
                return

            backtrack(i + 1)

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack()
        return ret


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, 2, 3], [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]),
        ([0], [[], [0]]),
    ],
)
def test_subsets(l1, expected):
    assert compare_nested_lists(Solution().subsets(l1), expected)
