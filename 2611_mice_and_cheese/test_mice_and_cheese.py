# https://leetcode.com/problems/mice-and-cheese
import heapq

import pytest


class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:
        return self.miceAndCheese_heap(reward1, reward2, k)

    @staticmethod
    def miceAndCheese_heap(reward1: list[int], reward2: list[int], k: int) -> int:
        output = 0
        n = len(reward1)
        heap = []
        for i in range(n):
            heap.append((reward2[i] - reward1[i], i))

        heapq.heapify(heap)
        visited = set()
        while k:
            k -= 1
            _, idx = heapq.heappop(heap)
            visited.add(idx)
            output += reward1[idx]

        # If there is anything left that has not been taken, we take it from reward2.
        for idx, val in enumerate(reward2):
            if idx in visited:
                continue
            output += val

        return output

    @staticmethod
    def miceAndCheese_dp(reward1: list[int], reward2: list[int], k: int) -> int:
        n = len(reward1)
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for j in range(1, k + 1):
            dp[n][j] = float("-inf")

        for i in range(n - 1, -1, -1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = dp[i + 1][j] + reward2[i]
                    continue

                take1 = dp[i + 1][j - 1] if j > 0 else float("-inf")
                take2 = dp[i + 1][j]

                dp[i][j] = max(take1 + reward1[i], take2 + reward2[i])

        return dp[0][k]

    @staticmethod
    def miceAndCheese_mine(reward1: list[int], reward2: list[int], k: int) -> int:
        def dfs(index, num_choices, curr_weight):
            if (2 * num_choices) == k:
                return curr_weight

            if index > len(reward2) and index > len(reward1):
                return curr_weight

            next_index = index + 1

            m1, m2, m3 = 0, 0, 0

            # choose reward1[index]for mouse 1
            if len(reward1) > next_index and next_index not in index_choices:
                index_choices[next_index] = True
                m1 = dfs(next_index, num_choices + 1, curr_weight + reward1[next_index])
                del index_choices[next_index]
            # choose reward2[index] for mouse 2
            if len(reward2) > next_index and next_index not in index_choices:
                index_choices[next_index] = True
                m2 = dfs(next_index, num_choices + 1, curr_weight + reward2[next_index])
                del index_choices[next_index]
            # neither choose
            m3 = dfs(index + 1, num_choices, curr_weight)

            return max(m1, m2, m3)

        index_choices = {}

        return dfs(0, 0, 0)


@pytest.mark.parametrize(
    "reward1,reward2,k,expected",
    [
        ([1, 1, 3, 4], [4, 4, 1, 1], 2, 15),
        ([1, 1], [1, 1], 2, 2),
    ],
)
def test_miceAndCheese(reward1, reward2, expected, k):
    assert Solution().miceAndCheese(reward1, reward2, k) == expected
