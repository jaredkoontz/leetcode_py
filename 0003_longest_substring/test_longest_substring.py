# https://leetcode.com/problems/longest-substring-without-repeating-characters
import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.lengthOfLongestSubstring_theirs(s)

    @staticmethod
    def lengthOfLongestSubstring_theirs(s: str) -> int:
        char_set = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            result = max(result, right - left + 1)

        return result

    @staticmethod
    def lengthOfLongestSubstring_mine(s: str) -> int:
        curr_longest = ""
        curr = ""
        length = len(s)
        index = 0
        while index < length:
            if s[index] in curr:
                if len(curr) > len(curr_longest):
                    curr_longest = curr
                index = index - (len(curr) - 1)
                curr = ""
            else:
                curr += s[index]
                index += 1
        return max(len(curr_longest), len(curr))


@pytest.mark.parametrize(
    "s,expected",
    [
        (" ", 1),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("abcdefghijklmnopabcdefghijklmnopabcdefghijklmnop", 16),
        ("", 0),
        ("dvdf", 3),
        ("aab", 2),
        ("abcd", 4),
        ("aa", 1),
        ("abcabcbb", 3),
        ("bbbbbbb", 1),
        ("pwwkew", 3),
    ],
)
def test_longest_substring(s, expected):
    assert Solution().lengthOfLongestSubstring(s) == expected
