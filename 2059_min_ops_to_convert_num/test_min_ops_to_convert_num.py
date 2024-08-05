from collections import deque

import pytest


class Solution:
    def minimumOperations(self, nums: list[int], start: int, goal: int) -> int:
        return self.minimumOperations_bfs(nums, start, goal)

    def minimumOperations_bfs(self, nums: list[int], start: int, goal: int) -> int:
        queue = deque([(start, 0)])
        visited = set()
        while queue:
            current_num, moves = queue.popleft()

            for num in nums:
                for value in (current_num + num, current_num - num, current_num ^ num):
                    if value == goal:
                        return moves + 1
                    if value not in visited and 0 <= value <= 1000:
                        visited.add(value)
                        queue.append((value, moves + 1))
        return -1


@pytest.mark.parametrize(
    "nums,start,goal,expected",
    [
        ([2, 4, 12], 2, 12, 2),
        ([3, 5, 7], 0, -4, 2),
        ([2, 8, 16], 0, 1, -1),
    ],
)
def test_min_ops_to_convert_num(nums, start, goal, expected) -> None:
    assert Solution().minimumOperations(nums, start, goal) == expected
