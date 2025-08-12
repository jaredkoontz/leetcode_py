# https://leetcode.com/problems/product-of-array-except-self
import pytest


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        assert (
                self.productExceptSelf_pre_suf_mine(nums)
                == self.productExceptSelf_pre_suf_optimal(nums)
                == self.productExceptSelf_pre_suf(nums)
                == self.productExceptSelf_brute_force(nums)
                == self.productExceptSelf_neet(nums)
                == self.productExceptSelf_final(nums)
        )
        return self.productExceptSelf_final(nums)

    @staticmethod
    def productExceptSelf_final(nums: list[int]) -> list[int]:
        length = len(nums)
        products = [1] * length
        for i in range(1, length):
            products[i] = nums[i - 1] * products[i - 1]

        right = nums[-1]
        for i in range(length - 2, -1, -1):
            products[i] *= right
            right *= nums[i]
        return products

    @staticmethod
    def productExceptSelf_neet(nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

    @staticmethod
    def productExceptSelf_pre_suf_mine(nums: list[int]) -> list[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        l_pointer = 1
        r_pointer = 1

        for i, num in enumerate(nums):
            left[i] = l_pointer
            j = -i - 1
            right[j] = r_pointer
            l_pointer *= nums[i]
            r_pointer *= nums[j]

        return [l_pointer * r_pointer for l_pointer, r_pointer in zip(left, right)]

    @staticmethod
    def productExceptSelf_pre_suf_optimal(nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n  # Initialize the result array with 1

        curr = 1
        # Calculate prefix product and store directly in ans
        for i in range(n):
            ans[i] = curr
            curr *= nums[i]

        curr = 1
        # Calculate suffix product and multiply with prefix to get the final answer
        for i in range(n - 1, -1, -1):
            ans[i] *= curr
            curr *= nums[i]

        return ans

    @staticmethod
    def productExceptSelf_pre_suf(nums: list[int]) -> list[int]:
        n = len(nums)

        # Initialize prefix and suffix arrays
        pre = [1] * n
        suff = [1] * n

        # Calculate prefix product
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]

        # Calculate suffix product
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]

        # Combine prefix and suffix products to get the result
        ans = [pre[i] * suff[i] for i in range(n)]

        return ans

    @staticmethod
    def productExceptSelf_brute_force(nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n

        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                product *= nums[j]
            ans[i] = product

        return ans


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([1, 2], [2, 1]),
    ],
)
def test_product_of_array(nums, expected):
    assert Solution().productExceptSelf(nums) == expected
