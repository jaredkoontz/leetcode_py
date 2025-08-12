# https://leetcode.com/problems/maximum-score-words-formed-by-letters
import collections

import pytest


class Solution:
    def maxScoreWords(
        self, words: list[str], letters: list[str], score: list[int]
    ) -> int:
        return self.maxScoreWords_mine(words, letters, score)

    @staticmethod
    def maxScoreWords_mine(
        words: list[str], letters: list[str], score: list[int]
    ) -> int:
        def backtrack(my_words, my_count, my_score, index):
            max_score = 0
            for i in range(index, len(my_words)):
                res = 0
                is_valid = True
                for ch in my_words[i]:
                    letter_score = ord(ch) - ord("a")
                    my_count[letter_score] -= 1
                    res += my_score[letter_score]
                    if my_count[letter_score] < 0:
                        is_valid = False

                if is_valid:
                    res += backtrack(my_words, my_count, my_score, i + 1)
                    max_score = max(res, max_score)

                for ch in my_words[i]:
                    my_count[ord(ch) - ord("a")] += 1

            return max_score

        if not words or not letters or not score:
            return 0

        count = [0] * len(score)
        for character in letters:
            count[ord(character) - ord("a")] += 1

        return backtrack(words, count, score, 0)

    def maxScoreWords_concise(
        self, words: list[str], letters: list[str], score: list[int]
    ) -> int:
        def _create_word_scores(my_score, my_words):
            word_scores = []
            for word in my_words:
                word_score = 0
                for c in word:
                    letter = ord(c) - ord("a")
                    char_score = my_score[letter]
                    word_score += char_score
                word_scores.append(word_score)
            return word_scores

        self.max_score = 0
        words_score = _create_word_scores(score, words)
        words_counter = [collections.Counter(word) for word in words]

        def dfs(i: int, curr_score: int, counter: collections.Counter) -> None:
            if curr_score + sum(words_score[i:]) <= self.max_score:
                return
            self.max_score = max(self.max_score, curr_score)
            for j, word_count in enumerate(words_counter[i:], i):
                if all(n <= counter.get(c, 0) for c, n in word_count.items()):
                    dfs(j + 1, curr_score + words_score[j], counter - word_count)

        dfs(0, 0, collections.Counter(letters))
        return self.max_score


@pytest.mark.parametrize(
    "words, letters, score, expected",
    [
        (
            ["dog", "cat", "dad", "good"],
            ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
            [
                1,
                0,
                9,
                5,
                0,
                0,
                3,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            23,
        ),
        (
            ["xxxz", "ax", "bx", "cx"],
            ["z", "a", "b", "c", "x", "x", "x"],
            [
                4,
                4,
                4,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                5,
                0,
                10,
            ],
            27,
        ),
        (
            ["leetcode"],
            ["l", "e", "t", "c", "o", "d"],
            [
                0,
                0,
                1,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            0,
        ),
    ],
)
def test_maxScoreWords(words, letters, score, expected):
    assert Solution().maxScoreWords(words, letters, score) == expected
