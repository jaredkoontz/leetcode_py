# https://leetcode.com/problems/asteroid-collision
import pytest


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        return self.asteroidCollision_stack(asteroids)

    @staticmethod
    def asteroidCollision_mine(asteroids: list[int]) -> list[int]:
        stack = []

        for i in asteroids:
            if stack and stack[-1] > 0 > i:
                while stack and stack[-1] > 0 > i and abs(stack[-1]) < abs(i):
                    stack.pop()

                if stack and stack[-1] > 0 > i and abs(stack[-1]) > abs(i):
                    continue
                elif stack and stack[-1] > 0 > i and stack[-1] == i * -1:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

        return stack

    @staticmethod
    def asteroidCollision_stack(asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            # We only need to resolve collisions under the following conditions:
            # - stack is non-empty
            # - current asteroid is -ve
            # - top of the stack is +ve
            while len(stack) and asteroid < 0 < stack[-1]:
                # Both asteroids are equal, destroy both.
                if stack[-1] == -asteroid:
                    stack.pop()
                    break
                # Stack top is smaller, remove the +ve asteroid
                # from the stack and continue the comparison.
                elif stack[-1] < -asteroid:
                    stack.pop()
                    continue
                # Stack top is larger, -ve asteroid is destroyed.
                elif stack[-1] > -asteroid:
                    break
            else:
                # -ve asteroid made it all the way to the
                # bottom of the stack and destroyed all asteroids.
                stack.append(asteroid)
        return stack


@pytest.mark.parametrize(
    "asteroids,expected",
    [
        ([5, 10, -5], [5, 10]),
        ([5, 10, -5, -5], [5, 10]),
        ([5, 10, -5, -6], [5, 10]),
        ([8, -8], []),
        ([10, 2, -5], [10]),
    ],
)
def test_asteroidCollision(asteroids, expected):
    assert Solution().asteroidCollision(asteroids) == expected
