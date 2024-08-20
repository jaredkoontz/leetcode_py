from collections import defaultdict
from copy import deepcopy
from typing import MutableSet
from typing import Tuple

import pytest

from helpers.testing_helpers import compare_nested_lists


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        return self.combinationSum2_dp(candidates, target)

    # todo failing because of wrong types
    @staticmethod
    def combinationSum2_dp(candidates: list[int], target: int) -> list[list[int]]:
        # unique_combos_with_sum[i] contains the unique combinations of candidates that sum to 'i'.
        unique_combos_with_sum: dict[int, MutableSet[Tuple]] = defaultdict(set)
        unique_combos_with_sum[0].add(())  # Base case.

        for candidate in sorted(candidates):
            # We don't want to modify unique_combos_with_sum while we're iterating over it,
            # so create a deep copy first.
            for existingComboSum, existing_combos in deepcopy(
                unique_combos_with_sum
            ).items():
                # Create new combos by adding 'candidate' to each existing combo.
                new_combo_sum: int = existingComboSum + candidate

                # We only care about new combos with sum <= target.
                if new_combo_sum <= target:
                    for existing_combo in existing_combos:
                        # Always add candidate to the END of existing_combo. This--along
                        # with sorting the candidates above--ensures that elements in a combo
                        # always appear in increasing order. So, for example, we'll always
                        # get (1,2,5) and not (2,1,5) or (5,2,1).
                        # This is important because we're using hash sets to reject duplicates,
                        # and two Python tuples will only yield the same hashes if they have
                        # the same elements, IN THE SAME ORDER.
                        unique_combos_with_sum[new_combo_sum].add(
                            existing_combo + (candidate,)
                        )
        return [list(combo) for combo in unique_combos_with_sum[target]]

    @staticmethod
    def combinationSum2_backtrack(
        candidates: list[int], target: int
    ) -> list[list[int]]:
        candidates.sort()
        ret = []

        def dfs(position, curr, my_target):
            if my_target == 0:
                ret.append(curr[:])
            if my_target <= 0:
                return
            prev = -1
            for i in range(position, len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                dfs(i + 1, curr, my_target - candidates[i])
                curr.pop()
                prev = candidates[i]

            return

        dfs(0, [], target)
        return ret


@pytest.mark.parametrize(
    "candidates,target,expected",
    [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
    ],
)
def test_combinationSum2(candidates, target, expected):
    assert compare_nested_lists(
        Solution().combinationSum2(candidates, target), expected
    )
