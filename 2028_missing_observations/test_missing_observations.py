# https://leetcode.com/problems/find-missing-observations
import pytest


class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        return self.missingRolls_math(rolls, mean, n)

    @staticmethod
    def missingRolls_math(rolls: list[int], mean: int, n: int) -> list[int]:
        """
        example:
        rolls=[3,2,4,3],mean=4,n=2
        totalobservations=m+n=4+2=6
        sumofobservations=4∗6=24
        sumofgivendicerolls=6∗2=12
        sumofremainingdicerolls=24−12=12

        """
        sum_rolls = sum(rolls)
        total_dice = n + len(rolls)
        # Find the remaining sum.
        remaining_sum = (mean * total_dice) - sum_rolls
        # Check if sum is valid or not.
        if remaining_sum > 6 * n or remaining_sum < n:
            return []
        distribute_mean = remaining_sum // n
        mod = remaining_sum % n
        # Distribute the remaining mod elements in n_elements list.
        n_elements = [distribute_mean] * n
        for i in range(mod):
            n_elements[i] += 1
        return n_elements

    @staticmethod
    def missingRolls_naive(rolls: list[int], mean: int, n: int) -> list[int]:
        possibilities = [1] * n
        final_possibility = []

        def dfs(curr_possibilities, curr_index):
            if (sum(rolls) + sum(possibilities)) / (len(rolls) + n) == mean:
                nonlocal final_possibility
                final_possibility = curr_possibilities
            else:
                # increment value at curr position if possible
                if possibilities[curr_index] < 6:
                    possibilities[curr_index] += 1
                    dfs(curr_possibilities, curr_index)
                # increment curr_index
                if curr_index + 1 < len(possibilities):
                    dfs(curr_possibilities, curr_index + 1)

        dfs(possibilities, 0)
        return final_possibility


@pytest.mark.parametrize(
    "rolls,mean,n,expected",
    [
        ([3, 2, 4, 3], 4, 2, [6, 6]),
        ([1, 5, 6], 3, 4, [3, 2, 2, 2]),
        ([1, 2, 3, 4], 6, 4, []),
    ],
)
def test_missingRolls(rolls, mean, n, expected):
    assert Solution().missingRolls(rolls, mean, n) == expected
