# https://leetcode.com/problems/design-a-stack-with-increment-operation
import pytest


class CustomStackLazyIncrement:
    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val


class CustomStackTheirs:
    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.top = -1
        self.incrementArr = [0] * maxSize

    def push(self, x: int) -> None:
        if self.top < len(self.stack) - 1:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top < 0:
            return -1

        res = self.stack[self.top] + self.incrementArr[self.top]
        if self.top > 0:
            self.incrementArr[self.top - 1] += self.incrementArr[self.top]
        self.incrementArr[self.top] = 0
        self.top -= 1
        return res

    def increment(self, k: int, val: int) -> None:
        if self.top >= 0:
            index = min(self.top, k - 1)
            self.incrementArr[index] += val


class CustomStackMine:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == self.max_size:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        num_to_update = len(self.stack) if k > len(self.stack) else k
        for i in range(num_to_update):
            self.stack[i] += val


CustomStack = CustomStackMine


@pytest.mark.parametrize(
    "operations, init, expected",
    [
        (
                [
                    "CustomStack",
                    "push",
                    "push",
                    "pop",
                    "push",
                    "push",
                    "push",
                    "increment",
                    "increment",
                    "pop",
                    "pop",
                    "pop",
                    "pop",
                ],
                [[3], [1], [2], [], [2], [3], [4], [5, 100], [2, 100], [], [], [], []],
                [None, None, None, 2, None, None, None, None, None, 103, 202, 201, -1],
        ),
    ],
)
def test_custom_stack(operations, init, expected):
    median_finder = None
    for op, components, curr_val in zip(operations, init, expected):
        if op == "CustomStack":
            median_finder = CustomStack(components[0])
        elif op == "push":
            assert median_finder.push(components[0]) == curr_val
        elif op == "pop":
            assert median_finder.pop() == curr_val
        else:
            assert median_finder.increment(components[0], components[1]) == curr_val
