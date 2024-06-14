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
        high = n
        while True:
            pick = (high + low) // 2
            guess_result = self.guess(pick)
            if guess_result == 0:
                return pick
            elif guess_result == -1:
                # less than my guess
                high = pick + 1
            else:
                # greater than my pick
                low = pick - 1


@pytest.mark.parametrize(
    "n,pick",
    [
        (10, 6),
        (
            1,
            1,
        ),
        (2, 1),
        (100000, 69),
    ],
)
def test_guessNumber(n, pick):
    s = Solution()
    s.MY_PICK = pick
    assert s.guessNumber(n) == pick
