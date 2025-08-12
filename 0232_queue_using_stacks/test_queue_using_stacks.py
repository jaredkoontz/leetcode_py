# https://leetcode.com/problems/implement-queue-using-stacks
import pytest


class StackQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


MyQueue = StackQueue


@pytest.mark.parametrize(
    "operations, init, expected",
    [
        (
                ["MyQueue", "push", "push", "peek", "pop", "empty"],
                [[], [1], [2], [], [], []],
                [None, None, None, 1, 1, False],
        ),
    ],
)
def test_queue_using_stacks(operations, init, expected):
    queue = None
    for op, components, curr_val in zip(operations, init, expected):
        if op == "MyQueue":
            queue = MyQueue()
        elif op == "push":
            assert queue.push(components[0]) == curr_val
        elif op == "pop":
            assert queue.pop() == curr_val
        elif op == "empty":
            assert queue.empty() == curr_val
        elif op == "peek":
            assert queue.peek() == curr_val
        else:
            assert False
