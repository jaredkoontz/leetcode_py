import pytest


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return self.wordPattern_mine(pattern, s)

    @staticmethod
    def wordPattern_mine(pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        mappings = {}
        exist_words = set()

        for pt, word in zip(pattern, words):
            if pt in mappings:
                if mappings[pt] != word:
                    return False
                continue

            if word in exist_words:
                return False

            mappings[pt] = word
            exist_words.add(word)

        return True


@pytest.mark.parametrize(
    "pattern, s, expected",
    [
        ("ab", "happy hacking", True),
        ("aaa", "aa aa aa aa", False),
        ("abba", "dog dog dog dog", False),
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
    ],
)
def test_word_pattern(pattern, s, expected):
    assert Solution().wordPattern(pattern, s) == expected
