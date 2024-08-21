from collections import deque

import pytest


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        return self.predictPartyVictory_queue(senate)

    @staticmethod
    def predictPartyVictory_two_queue(senate: str) -> str:
        senate = list(senate)
        n = len(senate)

        r_q, d_q = deque(), deque()
        for i, c in enumerate(senate):
            if c == "R":
                r_q.append(i)
            else:
                d_q.append(i)
        while r_q and d_q:
            curr_r = r_q.popleft()
            curr_d = d_q.popleft()

            if curr_r < curr_d:
                r_q.append(curr_d + n)
            else:
                d_q.append(curr_r + n)

        return "Radiant" if r_q else "Dire"

    @staticmethod
    def predictPartyVictory_queue(senate: str) -> str:
        radiant = "r"
        dire = "d"
        to_str = {radiant: "Radiant", dire: "Dire"}
        queue = deque()
        for x in senate:
            queue.append(x.lower())
        while True:
            senator = queue.popleft()
            opponent = radiant if senator == dire else dire
            try:
                queue.remove(opponent)
            except ValueError:
                return to_str[senator]
            queue.append(senator)
            if len(queue) == 1:
                return to_str[queue.popleft()]


@pytest.mark.parametrize(
    "senate,expected",
    [
        ("DDRRR", "Dire"),
        ("RD", "Radiant"),
        ("RDD", "Dire"),
    ],
)
def test_predictPartyVictory(senate, expected):
    assert Solution().predictPartyVictory(senate) == expected
