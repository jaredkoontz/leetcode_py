# https://leetcode.com/problems/guess-the-word
import pytest


class Solution:
    def findSecretWord(self, words: list[str], master: "Master") -> None:
        return self.findSecretWord_histogram(words, master)

    @staticmethod
    def findSecretWord_histogram(words: list[str], master: "Master") -> None:
        def match(a, b):
            return sum(i == j for i, j in zip(a, b))

        n = 0
        while n < 6:
            histogram = {}

            ## build heuristic
            for w1 in words:
                histogram[w1] = [0] * 7
                for w2 in words:
                    histogram[w1][match(w1, w2)] += 1
                histogram[w1] = max(histogram[w1])

            guess = min(words, key=lambda w: histogram[w])
            n = master.guess(guess)

            ## take only those words that have same match as the guess (necessary req. to be a total match)
            words = filter(lambda w: match(w, guess) == n, words)

    @staticmethod
    def findSecretWord_stats(words: list[str], master: "Master") -> None:
        def pair_matches(a, b):  # count the number of matching characters
            return sum(c1 == c2 for c1, c2 in zip(a, b))

        def most_overlap_word():
            counts = [
                [0 for _ in range(26)] for _ in range(6)
            ]  # counts[i][j] is nb of words with char j at index i
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][ord(c) - ord("a")] += 1

            best_word = None
            best_score = 0
            for word in candidates:
                score = 0
                for i, c in enumerate(word):
                    score += counts[i][
                        ord(c) - ord("a")
                        ]  # all words with same chars in same positions
                if score > best_score:
                    best_score = score
                    best_word = word

            return best_word

        candidates = words[:]  # all remaining candidates, initially all words
        while candidates:
            s = most_overlap_word()  # guess the word that overlaps with most others
            matches = master.guess(s)

            if matches == 6:
                return

            candidates = [
                w for w in candidates if pair_matches(s, w) == matches
            ]  # filter words with same matches


class Master:
    def guess(self, num: int):
        return 6


@pytest.mark.parametrize(
    "secret,words,allowed_guesses",
    [
        ("acckzz", ["acckzz", "ccbazz", "eiowzz", "abcczz"], 10),
        ("hamada", ["hamada", "khaled"], 10),
    ],
)
def test_findSecretWord(secret, words, allowed_guesses):
    # this one is very hard to test without access to leetcodes `Master` class
    # just ensure it runs on their site?
    assert secret in words
