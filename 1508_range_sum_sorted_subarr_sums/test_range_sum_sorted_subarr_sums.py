import heapq

import pytest


class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        return self.rangeSum_neet(nums, n, left, right)

    @staticmethod
    def rangeSum_neet(nums: list[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        left, right = left - 1, right - 1

        min_heap = [(num, index) for index, num in enumerate(nums)]
        heapq.heapify(min_heap)

        res = 0
        for i in range(right + 1):
            num, index = heapq.heappop(min_heap)
            if i >= left:
                res = (res + num) % mod
            if index + 1 < n:
                next_pair = (num + nums[index + 1], index + 1)
                heapq.heappush(min_heap, next_pair)
        return res

    @staticmethod
    def rangeSum_sliding_bin_search(nums, n, left, right):
        mod = 10**9 + 7

        def count_and_sum(my_nums, length, target):
            count = 0
            current_sum = 0
            total_sum = 0
            window_sum = 0
            i = 0
            for j in range(length):
                current_sum += my_nums[j]
                window_sum += my_nums[j] * (j - i + 1)
                while current_sum > target:
                    window_sum -= current_sum
                    current_sum -= my_nums[i]
                    i += 1
                count += j - i + 1
                total_sum += window_sum
            return count, total_sum

        def sum_of_first_k(my_nums, length, k):
            min_sum = min(my_nums)
            max_sum = sum(my_nums)
            bin_left = min_sum
            bin_right = max_sum

            while bin_left <= bin_right:
                mid = bin_left + (bin_right - bin_left) // 2
                if count_and_sum(my_nums, length, mid)[0] >= k:
                    bin_right = mid - 1
                else:
                    bin_left = mid + 1
            count, total_sum = count_and_sum(my_nums, length, bin_left)
            # There can be more subarrays with the same sum of left.
            return total_sum - bin_left * (count - k)

        result = (
            sum_of_first_k(nums, n, right) - sum_of_first_k(nums, n, left - 1)
        ) % mod
        # Ensure non-negative result
        return (result + mod) % mod

    @staticmethod
    def rangeSum_brute_force(nums: list[int], n: int, left: int, right: int) -> int:
        def get_sub_arr():
            sub_arr = []
            for index in range(n):
                curr_sum = 0
                # Iterate through all indices ahead of the current index.
                for j in range(index, n):
                    curr_sum += nums[j]
                    sub_arr.append(curr_sum)

                # Sort all subarray sum values in increasing order.
            return sorted(sub_arr)

        store_subarray = get_sub_arr()

        # Find the sum of all values between left and right.
        range_sum = 0
        mod = 10**9 + 7
        for i in range(left - 1, right):
            range_sum = (range_sum + store_subarray[i]) % mod
        return range_sum


@pytest.mark.parametrize(
    "nums,n,left,right,expected",
    [
        ([1, 2, 3, 4], 4, 1, 5, 13),
        ([1, 2, 3, 4], 4, 3, 4, 6),
        ([1, 2, 3, 4], 4, 1, 10, 50),
    ],
)
def test_range_sum(nums, n, left, right, expected):
    assert Solution().rangeSum(nums, n, left, right) == expected
