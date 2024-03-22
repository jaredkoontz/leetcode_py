import pytest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return self.strStr_actual(haystack, needle)

    @staticmethod
    def strStr_actual(haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1

        for i in range(len(haystack)):
            # no enough places for needle after i
            if i + len(needle) > len(haystack):
                break

            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1

    @staticmethod
    def strStr_lol(haystack: str, needle: str) -> int:
        return haystack.find(needle)


@pytest.mark.parametrize(
    "needle,haystack,expected",
    [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("leeto", "eeto", 1),
    ],
)
def test_first_occurrence_index(needle, haystack, expected):
    assert Solution().strStr(needle, haystack) == expected
