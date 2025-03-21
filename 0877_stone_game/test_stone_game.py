# https://leetcode.com/problems/stone-game/
# fun fact, you can just have `return True` on this problem and get 100%
from collections import deque

import pytest


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        return self.stoneGame_rec(piles)

    @staticmethod
    def stoneGame_rec(piles: list[int]) -> bool:
        alice = []
        bob = []

        def takes(leftPile):
            if not leftPile:
                return
            if len(leftPile) & 1 == 0:
                idx = 0 if leftPile[0] > leftPile[-1] else -1
                alice.append(leftPile[idx])
            else:
                if len(leftPile) == 1:
                    idx = 0
                    bob.append(leftPile[idx])
                else:
                    idx = 0 if leftPile[0] <= leftPile[-1] else -1
                    bob.append(leftPile[idx])

            leftPile.pop(idx)
            takes(leftPile)

        takes(piles)

        return sum(alice) > sum(bob)

    @staticmethod
    def stoneGame_mine(piles: list[int]) -> bool:
        # Initial strategy
        # Given a list of piles, we only check where the greatest pile is between the two in the second to last
        # outer layer.
        # If both or neither left >= max(secondright, right) and right >= max(secondleft, left), we take the max between the two,
        # otherwise we take the one that satisfies the condition

        def move():
            if len(piles) == 1:
                score = piles.pop()
            elif (piles[0] >= max(piles[-1], piles[-2])) == (
                piles[-1] >= max(piles[0], piles[1])
            ):
                if piles[0] > piles[-1]:
                    score = piles.popleft()
                else:
                    score = piles.pop()
            elif piles[0] >= max(piles[-1], piles[-2]):
                score = piles.popleft()
            else:
                score = piles.pop()
            return score

        piles = deque(piles)
        final_score = 0

        # We take turns: alice adds, bob substracts
        i = 0
        while piles:
            turn_score = move()
            if i // 2 == 0:
                final_score += turn_score
            else:
                final_score -= turn_score
        return final_score > 0

    @staticmethod
    def stoneGame_works_for_leetcode(piles: list[int]) -> bool:
        # Try it 🤣🤣
        return True


@pytest.mark.parametrize(
    "piles,expected",
    [
        ([5, 3, 4, 5], True),
        ([2, 7, 2, 3], True),
    ],
)
def test_stoneGame(piles, expected):
    assert Solution().stoneGame(piles) == expected
