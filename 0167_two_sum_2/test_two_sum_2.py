import pytest

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        return self.twoSum_mine(numbers, target)

    @staticmethod
    def twoSum_mine(numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        l, r = 0, n - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return []

    @staticmethod
    def twoSum_dict(numbers: list[int], target: int) -> list[int]:
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i

    @staticmethod
    def twoSum_bin_search(numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
    ],
)
def test_two_sum(numbers, target, expected):
    assert Solution().twoSum(numbers, target) == expected
