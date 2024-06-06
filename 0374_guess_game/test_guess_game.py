import pytest


class Solution:
    MY_PICK = 6

    def guess(self, pick):
        if pick == self.MY_PICK:
            return 0
        if pick < self.MY_PICK:
            return 1
        else:
            return -1

    def guessNumber(self, n: int) -> int:
        low = 1
        high = n + 1
        while True:
            pick = (high + low) // 2
            guess_result = self.guess(pick)
            if guess_result == 0:
                return pick
            elif guess_result == -1:
                # less than my guess
                high = pick
            else:
                # greater than my pick
                low = pick


@pytest.mark.parametrize(
    "n,pick,expected",
    [
        (10, 6, 6),
        (1, 1, 1),
        (2, 1, 1),
    ],
)
def test_guessNumber(n, pick, expected):
    s = Solution()
    s.MY_PICK = pick
    assert s.guessNumber(n) == expected
