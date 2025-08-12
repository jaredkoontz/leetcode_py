# https://leetcode.com/problems/longest-palindrome
from collections import Counter

import pytest


class Solution:
    def longestPalindrome(self, s: str) -> int:
        return self.longestPalindrome_mine(s)

    @staticmethod
    def longestPalindrome_mine(s: str) -> int:
        counter = Counter(s)
        longest_palindrome = 0
        for count in counter.values():
            if count & 1 == 0:
                longest_palindrome += count
            else:
                longest_palindrome += count - 1 if longest_palindrome & 1 else count
        return longest_palindrome


@pytest.mark.parametrize(
    "s,expected",
    [
        ("abccccdd", 7),
        ("bb", 2),
        ("a", 1),
        (
            "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattle"
            "fiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivest"
            "hatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecann"
            "otconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourp"
            "oorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhatthey"
            "didhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonob"
            "lyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetake"
            "increaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthese"
            "deadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeopleb"
            "ythepeopleforthepeopleshallnotperishfromtheearth",
            983,
        ),
    ],
)
def test_longest_palindrome(s, expected):
    assert Solution().longestPalindrome(s) == expected
