# https://leetcode.com/problems/implement-stack-using-queues
from collections import deque

import pytest


class OneQueueStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        # Rotate the queue to make the last element to the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


class TwoQueueStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        # Step 1: Push to queue2
        self.queue2.append(x)

        # Step 2: Push all elements from queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())

        # Step 3: Swap names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1


MyStack = TwoQueueStack


@pytest.mark.parametrize(
    "operations, init, expected",
    [
        (
            ["MyStack", "push", "push", "top", "pop", "empty"],
            [[], [1], [2], [], [], []],
            [None, None, None, 2, 2, False],
        ),
    ],
)
def test_queue_using_stacks(operations, init, expected):
    queue = None
    for op, components, curr_val in zip(operations, init, expected):
        if op == "MyStack":
            queue = MyStack()
        elif op == "push":
            assert queue.push(components[0]) == curr_val
        elif op == "pop":
            assert queue.pop() == curr_val
        elif op == "empty":
            assert queue.empty() == curr_val
        elif op == "top":
            assert queue.top() == curr_val
        else:
            assert False
