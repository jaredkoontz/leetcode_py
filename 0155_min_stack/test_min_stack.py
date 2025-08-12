# https://leetcode.com/problems/min-stack
import sys

import pytest


class MinStack:
    def __init__(self):
        self.elements = []
        self.min = []
        self.min_val = sys.maxsize

    def push(self, val: int) -> None:
        self.elements.append(val)
        if self.min_val >= val:
            self.min.append(val)
            self.min_val = val

    def pop(self) -> None:
        pop_ele = self.elements.pop()
        if self.min_val == pop_ele:
            self.min.pop()
            if len(self.min) != 0:
                self.min_val = self.min[-1]
            else:
                self.min_val = sys.maxsize

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return self.min_val


class MinStack_mine:
    def __init__(self):
        self.stack = []
        self.curr_min = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.curr_min = min(self.curr_min, val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.curr_min:
                self.curr_min = min(self.stack) if self.stack else float("inf")

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return int(self.curr_min)


@pytest.mark.parametrize(
    "operations, values, expected",
    [
        (
                ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
                [[], [-2], [0], [-3], [], [], [], []],
                [None, None, None, None, -3, None, 0, -2],
        ),
        (
                [
                    "MinStack",
                    "push",
                    "push",
                    "push",
                    "top",
                    "pop",
                    "getMin",
                    "pop",
                    "getMin",
                    "pop",
                    "push",
                    "top",
                    "getMin",
                    "push",
                    "top",
                    "getMin",
                    "pop",
                    "getMin",
                ],
                [
                    [],
                    [2147483646],
                    [2147483646],
                    [2147483647],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [2147483647],
                    [],
                    [],
                    [-2147483648],
                    [],
                    [],
                    [],
                    [],
                ],
                [
                    None,
                    None,
                    None,
                    None,
                    2147483647,
                    None,
                    2147483646,
                    None,
                    2147483646,
                    None,
                    None,
                    2147483647,
                    2147483647,
                    None,
                    -2147483648,
                    -2147483648,
                    None,
                    2147483647,
                ],
        ),
    ],
)
def test_min_stack(operations, values, expected):
    min_stack = None
    for op, value, output in zip(operations, values, expected):
        if op == "MinStack":
            min_stack = MinStack()
        elif op == "push":
            min_stack.push(value[0])
        elif op == "pop":
            min_stack.pop()
        elif op == "top":
            assert output == min_stack.top()
        elif op == "getMin":
            assert output == min_stack.getMin()
