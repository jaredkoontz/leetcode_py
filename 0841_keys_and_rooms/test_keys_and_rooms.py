# https://leetcode.com/problems/keys-and-rooms
from collections import deque

import pytest


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        return self.canVisitAllRooms_dfs(rooms)

    @staticmethod
    def canVisitAllRooms_dfs(rooms: list[list[int]]) -> bool:
        room_nodes = rooms
        visited_rooms = set()
        visited_rooms.add(0)

        def dfs(room):
            for i in room_nodes[room]:
                if i not in visited_rooms:
                    visited_rooms.add(i)
                else:
                    continue
                dfs(i)

        dfs(0)

        if len(visited_rooms) == len(rooms):
            return True
        else:
            return False

    @staticmethod
    def canVisitAllRooms_bfs(rooms: list[list[int]]) -> bool:
        if len(rooms) == 0:
            return True

        queue = deque()
        visited = set()
        for key in rooms[0]:
            queue.append(key)
        visited.add(0)

        while queue:
            room = queue.popleft()
            if room not in visited:
                for key in rooms[room]:
                    queue.append(key)
                visited.add(room)
        return len(visited) == len(rooms)


@pytest.mark.parametrize(
    "rooms,expected",
    [
        ([[4], [3], [], [2, 5, 7], [1], [], [8, 9], [], [], [6]], False),
        ([[1], [2], [], [3]], False),
        ([[1], [2], [3], []], True),
        ([[1, 3], [3, 0, 1], [2], [0]], False),
    ],
)
def test_canVisitAllRooms(rooms, expected):
    assert Solution().canVisitAllRooms(rooms) == expected
