import pytest


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return self.reversePrefix_mine(word, ch)

    @staticmethod
    def reversePrefix_swap(word: str, ch: str) -> str:
        # Find the first occurrence of the character `ch`
        first_occurrence = word.find(ch)

        if first_occurrence == -1:
            # If the character `ch` is not found, return the word as is
            return word

        # Convert the word to a list of characters for easier manipulation
        word_list = list(word)

        # Reverse the prefix from the beginning of the word to the first occurrence of `ch`
        start = 0
        end = first_occurrence
        while start < end:
            # Swap the characters at `start` and `end`
            word_list[start], word_list[end] = word_list[end], word_list[start]
            start += 1
            end -= 1

        # Convert the list back to a string
        return "".join(word_list)

    @staticmethod
    def reversePrefix_mine(word: str, ch: str) -> str:
        index = word.find(ch)
        if index != -1:
            return word[: index + 1][::-1] + word[index + 1 :]
        return word


@pytest.mark.parametrize(
    "word,cd,expected",
    [
        ("abcdefd", "d", "dcbaefd"),
        ("xyxzxe", "z", "zxyxxe"),
        ("abcd", "z", "abcd"),
        ("abcdz", "z", "zdcba"),
    ],
)
def test_reverse_prefix(word, cd, expected):
    assert Solution().reversePrefix(word, cd) == expected
