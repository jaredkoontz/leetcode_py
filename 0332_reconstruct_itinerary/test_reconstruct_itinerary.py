# https://leetcode.com/problems/reconstruct-itinerary
from collections import defaultdict

import pytest


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        return self.findItinerary_iter(tickets)

    @staticmethod
    def findItinerary_iter(tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        stack = ["JFK"]
        itinerary = []

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            itinerary.append(stack.pop())

        return itinerary[::-1]

    @staticmethod
    def findItinerary_rec(tickets: list[list[str]]) -> list[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)

                if dfs(v):
                    return True

                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res


@pytest.mark.parametrize(
    "tickets,expected",
    [
        (
                [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
                ["JFK", "MUC", "LHR", "SFO", "SJC"],
        ),
        (
                [
                    ["JFK", "SFO"],
                    ["JFK", "ATL"],
                    ["SFO", "ATL"],
                    ["ATL", "JFK"],
                    ["ATL", "SFO"],
                ],
                ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
        ),
    ],
)
def test_findItinerary(tickets, expected):
    assert Solution().findItinerary(tickets) == expected
