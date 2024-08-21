import pytest


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        return self.twoSum_mine(numbers, target)

    @staticmethod
    def twoSum_mine(numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        left, right = 0, n - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                # +1 because for some reason leetcode wants 1 index 🤷
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
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
            left, right = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    left = mid + 1
                else:
                    right = mid - 1


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
