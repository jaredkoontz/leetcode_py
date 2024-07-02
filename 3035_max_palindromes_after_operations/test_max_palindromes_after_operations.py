from collections import Counter

import pytest


class Solution:
    def maxPalindromesAfterOperations(self, words: list[str]) -> int:
        return self.maxPalindromesAfterOperations_counter(words)

    @staticmethod
    def maxPalindromesAfterOperations_counter(words: list[str]) -> int:
        count = Counter(c for w in words for c in w)
        lengths = sorted(map(len, words))
        even = 0
        for c in count:
            even += count[c] // 2
        for i, length in enumerate(lengths):
            even -= length // 2
            if even < 0:
                return i
        return len(lengths)

    @staticmethod
    def maxPalindromesAfterOperations_odd(words: list[str]) -> int:
        n, odd_length, result = len(words), 0, len(words)
        lengths, freq = [], [0] * 26
        for word in words:
            lengths.append(len(word))
            odd_length += lengths[-1] & 1
            for ch in word:
                freq[ord(ch) - ord("a")] += 1
        odd_freq = len(list(filter(lambda x: x & 1, freq)))
        remaining = max(0, odd_freq - odd_length)
        lengths.sort(reverse=True)
        for i in range(n):
            if remaining <= 0:
                break
            remaining -= lengths[i] - (lengths[i] & 1)
            result -= 1
        return result


@pytest.mark.parametrize(
    "words,expected",
    [
        (["abbb", "ba", "aa"], 3),
        (["abc", "ab"], 2),
        (["cd", "ef", "a"], 1),
    ],
)
def test_max_palindromes_after_operations(words, expected):
    assert Solution().maxPalindromesAfterOperations(words) == expected
