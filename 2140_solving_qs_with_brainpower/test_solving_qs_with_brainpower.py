# https://leetcode.com/problems/solving-questions-with-brainpower
import pytest


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        return self.mostPoints_bottom_up(questions)

    @staticmethod
    def mostPoints_bottom_up(questions: list[list[int]]) -> int:
        # cache = collections.defaultdict(int)
        cache = {}

        for i in range(len(questions) - 1, -1, -1):
            points, brainpower = questions[i]
            index_temp = (i + brainpower) + 1
            cache[i] = max(cache.get((i + 1), 0), points + cache.get(index_temp, 0))

        return cache[0]

    @staticmethod
    def mostPoints_cache_neet(questions: list[list[int]]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(questions):
                return 0
            if i in dp:
                print("cached")
                return dp[i]
            points, brainpower = questions[i]
            index_temp = (i + brainpower) + 1

            dp[i] = max(dfs(i + 1), points + dfs(index_temp))
            return dp[i]

        return dfs(0)

    @staticmethod
    def mostPoints_dfs(questions: list[list[int]]) -> int:
        def dfs(curr_index, curr_points):
            if not (-1 < curr_index < len(questions)):
                return

            points, brainpower = questions[curr_index]

            print(f"{curr_index=} {curr_points=} {points=} {brainpower=}")

            # do question
            curr_points_temp = curr_points + points
            index_temp = (curr_index + brainpower) + 1
            most_points[0] = max(most_points[0], curr_points_temp)
            dfs(index_temp, curr_points_temp)

            # don't do question
            dfs(curr_index + 1, curr_points)

        most_points = [float("-inf")]

        dfs(0, 0)
        return most_points[0]


@pytest.mark.parametrize(
    "questions,expected",
    [
        ([[3, 2], [4, 3], [4, 4], [2, 5]], 5),
        ([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 7),
    ],
)
def test_mostPoints(questions, expected):
    assert Solution().mostPoints(questions) == expected
