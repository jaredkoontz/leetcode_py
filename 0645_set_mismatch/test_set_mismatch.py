# https://leetcode.com/problems/set-mismatch/
import pytest


class Solution:
        def findErrorNums(self, nums: list[int]) -> list[int]:
            return self.findErrorNums_sum(nums)

        @staticmethod
        def findErrorNums_xor(nums: list[int]) -> list[int]:
            n = len(nums)
            xor_all = 0
            xor_array = 0

            for i in range(1, n + 1):
                xor_all ^= i

            for num in nums:
                xor_array ^= num

            xor_result = xor_array ^ xor_all

            rightmost_set_bit = xor_result & -xor_result

            xor_set = 0
            xor_not_set = 0

            for i in range(1, n + 1):
                if (i & rightmost_set_bit) != 0:
                    xor_set ^= i
                else:
                    xor_not_set ^= i

            for num in nums:
                if (num & rightmost_set_bit) != 0:
                    xor_set ^= num
                else:
                    xor_not_set ^= num

            for num in nums:
                if num == xor_set:
                    return [xor_set, xor_not_set]

            return [xor_not_set, xor_set]

        @staticmethod
        def findErrorNums_sorted(nums: list[int]) -> list[int]:
            nums = sorted(nums)

            for i in range(1, len(nums) + 1):
                if i not in nums:
                    nums.append(i)
                else:
                    nums.remove(i)

            return nums

        @staticmethod
        def findErrorNums_mine(nums: list[int]) -> list[int]:
            n = len(nums)
            my_map = {i: 0 for i in range(1, n + 1)}

            for a in nums:
                my_map[a] -= 1

            duplicate, missing = 0, 0

            for key, value in my_map.items():
                if value == -1:
                    duplicate = key
                if value == 1:
                    missing = key

            return [duplicate, missing]

        @staticmethod
        def findErrorNums_sum(nums: list[int]) -> list[int]:
            n = len(nums)
            actual_sum = n * (n + 1) // 2
            array_sum,unique_sum = 0,0
            s = set()

            for i in nums:
                array_sum += i
                s.add(i)

            for i in s:
                unique_sum += i

            duplicate = array_sum - unique_sum
            missing = actual_sum - unique_sum

            return [duplicate, missing]
        @staticmethod
        def findErrorNums_list(nums: list[int]) -> list[int]:
            n = len(nums)
            v = [0] * (n + 1)
            missing, duplicate = 0, 0

            for num in nums:
                v[num] += 1

            for i in range(1, len(v)):
                if v[i] == 2:
                    duplicate = i
                if v[i] == 0:
                    missing = i

            return [duplicate, missing]
        @staticmethod
        def findErrorNums_naive(nums: list[int]) -> list[int]:
            dup, missing = -1, -1

            for i in range(1, len(nums) + 1):
                count = nums.count(i)
                if count == 2:
                    dup = i
                elif count == 0:
                    missing = i

            return [dup, missing]

@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1,2,2,4],[2,3]),
        ([1, 1], [1,2]),
        ([2, 2], [2,1]),
    ],
)
def test_max_product_two_elements(nums, expected):
    assert Solution().findErrorNums(nums) == expected
