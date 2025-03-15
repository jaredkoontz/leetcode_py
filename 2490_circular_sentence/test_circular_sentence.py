# https://leetcode.com/problems/circular-sentence/
import pytest


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        return self.isCircularSentence_mine(sentence)

    @staticmethod
    def isCircularSentence_mine(sentence: str) -> bool:
        tokens = sentence.split(" ")
        if not sentence or not tokens:
            return False
        if len(tokens) == 1:
            return tokens[0][0] == tokens[0][-1]
        if sentence[0] != sentence[len(sentence) - 1]:
            return False

        for i in range(1, len(tokens)):
            if tokens[i][0] != tokens[i - 1][-1]:
                return False

        return True

    @staticmethod
    def isCircularSentence_one_line(sentence: str) -> bool:
        return all(
            [sentence[0] == sentence[-1]]
            + [
                sentence[i - 1] == sentence[i + 1]
                for i in range(len(sentence))
                if sentence[i] == " "
            ]
        )


@pytest.mark.parametrize(
    "sentence,expected",
    [
        ("leetcode exercises sound delightful", True),
        ("eetcode", True),
        ("eetcodr", False),
        ("Leetcode is cool", False),
        ("", False),
        ("l", True),
        ("ab a", False),
    ],
)
def test_isCircularSentence(sentence, expected):
    assert Solution().isCircularSentence(sentence) is expected
