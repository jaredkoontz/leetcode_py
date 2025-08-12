# https://leetcode.com/problems/find-unique-binary-string
import pytest


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        return self.findDifferentBinaryString_base10(nums)

    @staticmethod
    def findDifferentBinaryString_dfs(nums: list[str]) -> str:
        ans = []

        def dfs(curr, path, visited):
            if len(path) == curr:
                if "".join(path) not in visited:
                    ans.append(path[:])
                    return ans
                return
            for i in range(2):
                s = str(i)

                path.append(s)
                dfs(curr, path, visited)
                path.pop()
                if len(ans) == 1:
                    return

        k = len(nums)
        vist = set(nums)
        dfs(k, [], vist)
        return "".join(ans[0])

    @staticmethod
    def findDifferentBinaryString_brute_force(nums: list[str]) -> str:
        def bin_generate(curr, length, my_bin_set):
            if len(curr) == length:
                return curr if curr not in my_bin_set else ""

            add_zero = bin_generate(curr + "0", length, my_bin_set)
            if add_zero:
                return add_zero

            return bin_generate(curr + "1", length, my_bin_set)

        n = len(nums)
        bin_set = set(nums)
        return bin_generate("", n, bin_set)

    @staticmethod
    def findDifferentBinaryString_base10(nums: list[str]) -> str:
        integers = {int(num, 2) for num in nums}
        num_bits = len(nums)

        for i in range(2 ** num_bits):
            if i not in integers:
                return bin(i)[2:].zfill(num_bits)

        return ""

    @staticmethod
    def findDifferentBinaryString_flip(nums: list[str]) -> str:
        ans = ""

        for i in range(len(nums)):
            current_char = nums[i][i]
            opposite_char = "1" if current_char == "0" else "0"

            # Append the opposite character to the result string
            ans += opposite_char

        return ans

    @staticmethod
    def findDifferentBinaryString_flip_one_line(nums: list[str]) -> str:
        return "".join("1" if nums[i][i] == "0" else "0" for i in range(len(nums)))


@pytest.mark.parametrize(
    "nums,expected",
    [
        (["10", "11"], "00"),
        (["01", "10"], "00"),
        (["01", "00"], "10"),
        (["111", "011", "001"], "000"),
    ],
)
def test_findDifferentBinaryString(nums, expected):
    assert Solution().findDifferentBinaryString(nums) == expected
