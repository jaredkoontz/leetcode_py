# https://leetcode.com/problems/rearrange-spaces-between-words
import pytest


class Solution:
    __slots__ = ()

    def reorderSpaces(self, text: str) -> str:
        return self.reorderSpaces_mine(text)

    @staticmethod
    def reorderSpaces_mine(text: str) -> str:
        words = text.split()
        total_spaces = text.count(" ")

        if len(words) > 1:
            spaces_between_words, remaining_spaces = divmod(
                total_spaces, (len(words) - 1)
            )
        else:
            spaces_between_words = 0
            remaining_spaces = total_spaces

        space_str = " " * spaces_between_words
        result = space_str.join(words)
        result += " " * remaining_spaces

        return result


@pytest.mark.parametrize(
    "text, expected",
    [
        ("  this   is  a sentence ", "this   is   a   sentence"),
        (" practice   makes   perfect", "practice   makes   perfect "),
    ],
)
def test_reorder(text, expected):
    assert Solution().reorderSpaces(text) == expected
