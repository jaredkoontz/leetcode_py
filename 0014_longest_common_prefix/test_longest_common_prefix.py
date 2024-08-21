# https://leetcode.com/problems/longest-common-prefix
import pytest


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        return self.longestCommonPrefix_sorted(strs)

    @staticmethod
    def longestCommonPrefix_mine(strs: list[str]) -> str:
        if not strs:
            return ""

        longest_common_prefix = ""

        all_strs_len = len(strs)
        curr_index = 0
        min_index = 999999999999
        for s in range(all_strs_len):
            min_index = min(min_index, len(strs[s]))

        while curr_index < min_index:
            curr_char = ""
            for string in strs:
                if not curr_char:
                    curr_char = string[curr_index]
                else:
                    if curr_char != string[curr_index]:
                        return longest_common_prefix
            longest_common_prefix += curr_char
            curr_index += 1

        return longest_common_prefix

    @staticmethod
    def longestCommonPrefix_sorted(strs: list[str]) -> str:
        ans = ""
        v = sorted(strs)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans


@pytest.mark.parametrize(
    "strs,expected",
    [
        (["flower", "flow", ""], ""),
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["foo", "foo", "foo,"], "foo"),
    ],
)
def test_longestCommonPrefix(strs, expected):
    assert Solution().longestCommonPrefix(strs) == expected
