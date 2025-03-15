# https://leetcode.com/problems/count-servers-that-communicate/
import pytest


class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        # return self.countServers_mine(grid)
        return self.countServers_greedy(grid)

    @staticmethod
    def countServers_greedy(grid: list[list[int]]) -> int:
        def _collect_row(row_num) -> list[int]:
            return grid[row_num]

        def _collect_col(col_num) -> list[int]:
            return [r[col_num] for r in grid if col_num < len(r)]

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        searched = set()
        row_map = [rows, _collect_row, "R"]
        col_map = [cols, _collect_col, "C"]

        for group_count, collection_method, group_type in (row_map, col_map):
            for curr_entry_num in range(group_count):
                group = collection_method(curr_entry_num)
                if group.count(1) >= 2:
                    for i, element in enumerate(group):
                        if element == 1:
                            if group_type == "R":
                                if (curr_entry_num, i) not in searched:
                                    searched.add((curr_entry_num, i))
                                    count += 1
                            else:
                                if (i, curr_entry_num) not in searched:
                                    searched.add((i, curr_entry_num))
                                    count += 1

        return count

    @staticmethod
    def countServers_mine(grid: list[list[int]]) -> int:
        communicable_servers_count = 0
        col_count = [0] * len(grid[0])
        last_server_in_row = [-1] * len(grid)

        # first pass to count servers in each row and column
        for row in range(len(grid)):
            server_count_in_row = 0
            for col in range(len(grid[0])):
                if grid[row][col]:
                    server_count_in_row += 1
                    col_count[col] += 1
                    last_server_in_row[row] = col

            # if there is more than one server in the row, increase the count
            if server_count_in_row != 1:
                communicable_servers_count += server_count_in_row
                last_server_in_row[row] = -1

        # second pass to check if servers can communicate
        for row in range(len(grid)):
            if last_server_in_row[row] != -1 and col_count[last_server_in_row[row]] > 1:
                communicable_servers_count += 1

        return communicable_servers_count


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([[1, 0], [0, 1]], 0),
        ([[1, 0], [1, 1]], 3),
        ([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4),
        ([[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0]], 3),
    ],
)
def test_longestPalindrome(grid, expected):
    assert Solution().countServers(grid) == expected
