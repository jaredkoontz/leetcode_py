# https://leetcode.com/problems/longest-palindromic-substring/
import functools

import pytest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.longestPalindrome_dp(s)

    @staticmethod
    def longestPalindrome_backtrack(s: str) -> str:
        """
        It takes a lot of effort to write such a long explanation, so please UpVote ⬆️ if this helps you.

        Approach 1: Brute Force

        Intuition:
        The obvious brute force solution is to pick all possible starting and ending positions for a substring and verify if it is a palindrome.
        There are a total of n^2 such substrings (excluding the trivial solution where a character itself is a palindrome).
        Since verifying each substring takes O(n) time, the run time complexity is O(n^3).

        Algorithm:
        1. Pick a starting index for the current substring which is every index from 0 to n-2.
        2. Now, pick the ending index for the current substring which is every index from i+1 to n-1.
        3. Check if the substring from ith index to jth index is a palindrome.
        4. If step 3 is true and length of substring is greater than maximum length so far, update maximum length and maximum substring.
        5. Print the maximum substring.

        Complexity Analysis:
        Time complexity: O(n^3)
        Space complexity: O(1)
        """

        longest = ""

        @functools.cache
        def dfs(left, right):
            if left > right:
                return
            if is_palindrome(s[left:right]):
                nonlocal longest
                if len(s[left:right]) > len(longest):
                    longest = s[left:right]
            dfs(left + 1, right)
            dfs(left, right - 1)

        def is_palindrome(substr):
            return substr == substr[::-1]

        dfs(0, len(s))
        return longest

    @staticmethod
    def longestPalindrome_center_expand(s: str) -> str:
        """
        Approach 2: Expand Around Center

        Intuition:
        To enumerate all palindromic substrings of a given string, we expand the string at each possible starting and ending position of a palindrome,
        and keep track of the length of the longest palindrome found.

        Approach:
        - A palindrome mirrors around its center. A palindrome can be expanded from its center, and there are only 2n - 1 such centers.
        - There are 2n - 1 centers because a palindrome's center can be between two letters, which gives rise to even-length palindromes.

        Algorithm:
        1. Initialize max_str = s[0] and max_len = 1.
        2. Iterate over the string. For each character:
           - Expand around it for odd-length palindromes.
           - Expand between it and the next character for even-length palindromes.
        3. Track the maximum length and substring.

        Complexity Analysis:
        Time complexity: O(n^2)
        Space complexity: O(1)
        """

        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str

    @staticmethod
    def longestPalindrome_dp(s: str) -> str:
        """
        Approach 3: Dynamic Programming

        Intuition:
        To improve over brute force, avoid unnecessary re-computation when validating palindromes.
        Example: If "bab" is a palindrome, then "ababa" is also a palindrome if the outer letters match.

        Algorithm:
        1. Initialize a boolean table dp[n][n] = False.
        2. Set dp[i][i] = True for all i (every character is a palindrome).
        3. Iterate over the string:
           - For each i, for each j < i:
             - If s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                 - Mark dp[j][i] = True
                 - Update max_len and max_str if necessary.

        Complexity Analysis:
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        if len(s) <= 1:
            return s

        max_len = 1
        max_str = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        max_str = s[j : i + 1]
        return max_str

    @staticmethod
    def longestPalindrome_manacher(s: str) -> str:
        """
        Approach 4: Manacher's Algorithm

        Intuition:
        Use palindrome properties to avoid unnecessary validations.
        Maintain a center and right boundary, using previously calculated values to determine if we can expand.
        Track max_len and max_str throughout.

        Algorithm:
        1. Transform the string by inserting '#' between characters and at ends.
        2. Initialize dp array, center, right boundary.
        3. Iterate through transformed string:
           - Use symmetry to set dp[i] if i < right.
           - Expand around i while characters match.
           - Update center and right if needed.
           - Update max_len and max_str accordingly.

        Complexity Analysis:
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if len(s) <= 1:
            return s

        max_len = 1
        max_str = s[0]
        s = "#" + "#".join(s) + "#"
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])
            while (
                i - dp[i] - 1 >= 0
                and i + dp[i] + 1 < len(s)
                and s[i - dp[i] - 1] == s[i + dp[i] + 1]
            ):
                dp[i] += 1
            if i + dp[i] > right:
                center = i
                right = i + dp[i]
            if dp[i] > max_len:
                max_len = dp[i]
                max_str = s[i - dp[i] : i + dp[i] + 1].replace("#", "")
        return max_str


@pytest.mark.parametrize(
    "s,expected",
    [
        ("babad", "aba"),
        ("cbbd", "bb"),
        ("abbcccbbbcaaccbababcbcabca", "cbababc"),
    ],
)
def test_longestPalindrome(s, expected):
    assert Solution().longestPalindrome(s) == expected
