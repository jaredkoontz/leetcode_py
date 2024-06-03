import pytest


class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        freq = {}

        def f(i: int) -> int:
            if i == len(nums):
                return 1
            # nums[i] not taken
            result = f(i + 1)

            # check if we can take nums[i]
            if nums[i] - k not in freq and nums[i] + k not in freq:
                freq[nums[i]] = freq.get(nums[i], 0) + 1
                # nums[i] taken
                result += f(i + 1)

                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
            return result

        # -1 for empty subset
        return f(0) - 1


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([2, 4, 6], 2, 4),
        ([1], 1, 1),
    ],
)
def test_beautifulSubsets(nums: list[int], k: int, expected: int) -> None:
    assert Solution().beautifulSubsets(nums, k) == expected
