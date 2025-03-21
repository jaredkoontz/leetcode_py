# https://leetcode.com/problems/destroying-asteroids
import heapq

import pytest


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        return self.asteroidsDestroyed_stack(mass, asteroids)

    @staticmethod
    def asteroidsDestroyed_stack(mass: int, asteroids: list[int]) -> bool:
        # Time: O(n)
        # Space: O(n)
        stack = []
        for a in asteroids:
            stack.append(a)
            while stack and stack[-1] <= mass:
                mass += stack.pop()
        return not stack

    @staticmethod
    def asteroidsDestroyed_sort(mass: int, asteroids: list[int]) -> bool:
        # Time: O(n log n)
        # Space: O(1)
        asteroids.sort()
        for asteroid in asteroids:
            if asteroid > mass:
                return False
            mass += asteroid
        return True

    @staticmethod
    def asteroidsDestroyed_heap(mass: int, asteroids: list[int]) -> bool:
        # Time: O(n)
        # Space: O(1)
        heapq.heapify(asteroids)
        while asteroids:
            candi = heapq.heappop(asteroids)
            if candi > mass:
                return False
            else:
                mass += candi
        return True


@pytest.mark.parametrize(
    "mass,asteroids,expected",
    [
        (10, [3, 9, 19, 5, 21], True),
        (5, [4, 9, 23, 4], False),
    ],
)
def test_asteroidsDestroyed(mass, asteroids, expected):
    assert Solution().asteroidsDestroyed(mass, asteroids) == expected
