# https://leetcode.com/problems/find-the-winner-of-the-circular-game
import pytest


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return self.findTheWinner_dp(n, k)

    @staticmethod
    def findTheWinner_simluation(n: int, k: int) -> int:
        circle = [i for i in range(1, n + 1)]
        index = 0
        while len(circle) != 1:
            next_to_remove = (index + k - 1) % len(circle)
            circle.pop(next_to_remove)
            index = next_to_remove
        return circle[0]

    @staticmethod
    def findTheWinner_recursion(n: int, k: int) -> int:
        def recursion(n, k):
            if n == 1:
                return 0
            return (recursion(n - 1, k) + k) % n

        return recursion(n, k) + 1

    @staticmethod
    def findTheWinner_dp(n: int, k: int) -> int:
        res = 0
        for player_num in range(2, n + 1):
            res: int = (res + k) % player_num
        return res + 1


@pytest.mark.parametrize(
    "n,k,expected",
    [
        (5, 2, 3),
        (6, 5, 1),
    ],
)
def test_find_winner(n, k, expected):
    assert Solution().findTheWinner(n, k) == expected
