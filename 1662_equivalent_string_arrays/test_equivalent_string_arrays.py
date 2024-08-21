import pytest


class StringArrIterator:
    def __init__(self, str_arr):
        self.str_arr = str_arr
        self.arr_idx = 0
        self.str_idx = 0

    def has_next(self):
        return self.arr_idx < len(self.str_arr)

    def next(self):
        char_at = self.str_arr[self.arr_idx][self.str_idx]
        self.str_idx += 1
        if self.str_idx == len(self.str_arr[self.arr_idx]):
            self.arr_idx += 1
            self.str_idx = 0
        return char_at


class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return self.arrayStringsAreEqual_iter(word1, word2)

    @staticmethod
    def arrayStringsAreEqual_lol(word1: list[str], word2: list[str]) -> bool:
        return "".join(word1) == "".join(word2)

    @staticmethod
    def arrayStringsAreEqual_iter(word1: list[str], word2: list[str]) -> bool:
        itr1 = StringArrIterator(word1)
        itr2 = StringArrIterator(word2)

        while itr1.has_next() and itr2.has_next():
            if itr1.next() != itr2.next():
                return False

        return not itr1.has_next() and not itr2.has_next()


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        (["ab", "c"], ["a", "bc"], True),
        (["a", "cb"], ["ab", "c"], False),
        (["abc", "d", "defg"], ["abcddefg"], True),
    ],
)
def test_arrayStringsAreEqual(word1, word2, expected):
    assert Solution().arrayStringsAreEqual(word1, word2) == expected
