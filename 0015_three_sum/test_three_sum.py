import pytest


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        return self.threeSum_two_pointer(nums)

    # todo does not pass lc
    def threeSum_map(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort the array
        if len(nums) < 3:
            return []  # If fewer than three elements, return empty list
        if nums[0] > 0:
            return []  # If the smallest element is positive, there's no way to get zero

        # Create hash map of indices
        hash_map = {num: idx for idx, num in enumerate(nums)}
        result = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break  # If the current number is positive, no further processing
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates

            for j in range(i + 1, len(nums) - 1):
                required = -1 * (nums[i] + nums[j])  # To make sum zero
                if required in hash_map and hash_map[required] > j:
                    result.append([nums[i], nums[j], required])
                # Skip to the last occurrence of the current number
                j = hash_map[nums[j]]

            # Skip to the last occurrence of the current number
            i = hash_map[nums[i]]

        return result

    def threeSum_two_pointer(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort the array
        if len(nums) < 3:
            return []  # If fewer than three elements, return empty list
        if nums[0] > 0:
            return []  # If the smallest element is positive, there's no way to get zero

        result = []
        length = len(nums)

        for i in range(length):
            if nums[i] > 0:
                break  # If the current number is positive, there's no way to reach zero
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates

            low = i + 1
            high = length - 1

            while low < high:
                current_sum = nums[i] + nums[low] + nums[high]
                if current_sum > 0:
                    high -= 1  # Move high pointer down
                elif current_sum < 0:
                    low += 1  # Move low pointer up
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    # Skip duplicates
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1

        return result


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_three_sum(nums, expected):
    assert Solution().threeSum(nums) == expected
