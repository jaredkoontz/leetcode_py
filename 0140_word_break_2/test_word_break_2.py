import pytest

from helpers.test_helpers import compare_flat_lists


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                result_of_the_rest = self.helper(s[len(word) :], wordDict, memo)
                for item in result_of_the_rest:
                    item = word + " " + item
                    res.append(item)
        memo[s] = res
        return res


@pytest.mark.parametrize(
    "s,words,expected",
    [
        (
            "catsanddog",
            ["cat", "cats", "and", "sand", "dog"],
            ["cats and dog", "cat sand dog"],
        ),
        (
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
            ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
        ),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
    ],
)
def test_wordBreak(s, words, expected):
    compare_flat_lists(Solution().wordBreak(s, words), expected)
