# https://leetcode.com/problems/number-of-recent-calls
from collections import deque

import pytest


class Ping:
    def __init__(self, time_sent):
        self.time_sent = time_sent


class RecentCounterMine:
    TIMEOUT_TIME = 3_000

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        p = Ping(t)
        self.queue.append(p)
        while True:
            need_to_evict = (t - self.queue[0].time_sent) > self.TIMEOUT_TIME
            if need_to_evict:
                self.queue.popleft()
            else:
                break
        return len(self.queue)


RecentCounter = RecentCounterMine


@pytest.mark.parametrize(
    "operations, init, expected",
    [
        (
                ["RecentCounter", "ping", "ping", "ping", "ping"],
                [[], [1], [100], [3001], [3002]],
                [None, 1, 2, 3, 3],
        ),
    ],
)
def test_recent_counter(operations, init, expected):
    rc = None
    for op, components, curr_expected in zip(operations, init, expected):
        if op == "RecentCounter":
            rc = RecentCounter()
        elif op == "ping":
            assert curr_expected == rc.ping(components[0])
        else:
            assert False
