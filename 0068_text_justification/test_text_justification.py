# https://leetcode.com/problems/text-justification
import pytest


class Solution:
    __slots__ = ()

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        return self.fullJustify_theirs(words, maxWidth)

    @staticmethod
    def fullJustify_theirs(words: list[str], maxWidth: int) -> list[str]:
        def reorderSpaces(text: str) -> str:
            spaces = text.count(" ")
            s = text.split(" ")

            while "" in s:
                s.remove("")

            if len(s) == 1:
                return s[0] + " " * spaces

            # min no of spaces between each word
            nsw = spaces // (len(s) - 1)
            # no. of spaces left
            nsl = spaces % (len(s) - 1)
            curr_result = ""
            for i in range(len(s)):
                if i != len(s) - 1:
                    curr_result += s[i] + " " * nsw
                    if nsl > 0:
                        curr_result += " "
                        nsl -= 1
                else:
                    curr_result += s[i]
            return curr_result

        result = []

        last = words.pop(0)
        while words:
            if len(last) + len(words[0]) >= maxWidth:
                t = last + " " * (maxWidth - len(last))
                last = words.pop(0)
                result.append(t)

            elif len(last) + len(words[0]) < maxWidth:
                last = last + " " + words.pop(0)
        result.append(last + " " * (maxWidth - len(last)))

        for i in range(len(result) - 1):
            result[i] = reorderSpaces(result[i])

        return result

        # todo finish

    @staticmethod
    def fullJustify_mine(words: list[str], maxWidth: int) -> list[str]:
        def justify_uneven_line(spaces, num_words_needing_space):
            usual_space = spaces // num_words_needing_space
            return [usual_space + 1] + [usual_space] * (num_words_needing_space - 1)

        def get_spaces_between_words(current_line: list[str]) -> list[int]:
            num_chars = 0
            for curr_word in current_line:
                num_chars += len(curr_word)

            spaces = maxWidth - num_chars
            num_words_needing_space = len(current_line) - 1
            spaces_between_words = spaces / num_words_needing_space
            if spaces_between_words != int(spaces_between_words):
                return justify_uneven_line(spaces, num_words_needing_space)
            else:
                return [int(spaces_between_words)] * num_words_needing_space

        def justify_curr_line(current_line: list[str]) -> str:
            final_line = ""
            for num_spaces, word in zip(
                    get_spaces_between_words(current_line), current_line[:-1]
            ):
                final_line += word + (" " * num_spaces)
            return final_line + current_line[-1]

        def justify_single_line(word: str) -> str:
            return f"{word:<{maxWidth}}"

        justified = []
        curr_width = 0
        curr_line = []
        for index in range(len(words)):
            if index == len(words) - 1:
                if curr_line:
                    justified.append(justify_curr_line(curr_line))
                justified.append(justify_single_line(words[index]))
            else:
                width = len(words[index])
                if curr_width + width > maxWidth:
                    if len(curr_line) == 1:
                        justified.append(justify_single_line(curr_line[0]))
                    else:
                        justified.append(justify_curr_line(curr_line))
                    curr_width = 0
                    curr_line = []

                curr_line = curr_line + [words[index]]
                # add +1 for the space after the word
                curr_width += width + 1

        return justified


@pytest.mark.parametrize(
    "words, maxWidth, expected",
    [
        (
                ["This", "is", "an", "example", "of", "text", "justification."],
                16,
                ["This    is    an", "example  of text", "justification.  "],
        ),
        (
                ["What", "must", "be", "acknowledgment", "shall", "be"],
                16,
                ["What   must   be", "acknowledgment  ", "shall be        "],
        ),
        (
                [
                    "Science",
                    "is",
                    "what",
                    "we",
                    "understand",
                    "well",
                    "enough",
                    "to",
                    "explain",
                    "to",
                    "a",
                    "computer.",
                    "Art",
                    "is",
                    "everything",
                    "else",
                    "we",
                    "do",
                ],
                20,
                [
                    "Science  is  what we",
                    "understand      well",
                    "enough to explain to",
                    "a  computer.  Art is",
                    "everything  else  we",
                    "do                  ",
                ],
        ),
    ],
)
def test_justify(words, maxWidth, expected):
    assert Solution().fullJustify(words, maxWidth) == expected
