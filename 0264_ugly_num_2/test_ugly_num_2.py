# https://leetcode.com/problems/ugly-number-ii
import heapq

import pytest


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return self.nthUglyNumber_dp(n)

    @staticmethod
    def nthUglyNumber_dp(n: int) -> int:
        """
        Time Complexity : O(N), Here loop creates the time Complexity. Where N is the given number n.

        Space Complexity : O(N), Array(dp) space.

        Solved using Dynamic Programming (Tabulation).
        """
        dp = [1] * n
        x = y = z = 0

        for i in range(1, n):
            dp[i] = min(dp[x] * 2, min(dp[y] * 3, dp[z] * 5))
            if dp[i] == dp[x] * 2:
                x += 1
            if dp[i] == dp[y] * 3:
                y += 1
            if dp[i] == dp[z] * 5:
                z += 1

        return dp[-1]

    @staticmethod
    def nthUglyNumber_hash_map(n: int) -> int:
        """
        Time Complexity : O(NlogN), The time complexity of the code is O(NlogN) since we are doing 3 insertion
        operations in a Hash Table (set) for each iteration in the loop N times, and
        insertion operations in a Hash Table (set) take logN time. Where N is the given number n.

        Space Complexity : O(N), Hash Table (set) space.

        Solved using a Hash Table.
        """
        ugly_set = {1}
        nth_number = 1

        for _ in range(n):
            nth_number = min(ugly_set)
            ugly_set.remove(nth_number)
            ugly_set.add(nth_number * 2)
            ugly_set.add(nth_number * 3)
            ugly_set.add(nth_number * 5)

        return nth_number

    @staticmethod
    def nthUglyNumber_heap(n: int) -> int:
        ugly_numbers = []
        heap = [1]
        visited = {1}

        factors = [2, 3, 5]

        for _ in range(n):
            current_ugly = heapq.heappop(heap)
            ugly_numbers.append(current_ugly)

            for factor in factors:
                new_ugly = current_ugly * factor
                if new_ugly not in visited:
                    visited.add(new_ugly)
                    heapq.heappush(heap, new_ugly)

        return ugly_numbers[-1]

    @staticmethod
    def nthUglyNumber_naive(n: int) -> int:
        """
        Time Complexity : O(K) where K is the nth ugly number.
        Because we are traversing the loop K times, the time complexity is O(K).

        Space Complexity : O(1), Constant space.
        """

        def _keeps_on_dividing_until_possible(dividend, divisor):
            while dividend % divisor == 0:
                dividend //= divisor
            return dividend

        i = 0
        count = 0
        while count < n:
            is_ugly = i + 1
            for factor in [2, 3, 5]:
                is_ugly = _keeps_on_dividing_until_possible(is_ugly, factor)
            if is_ugly == 1:
                count += 1
            i += 1
        return i


@pytest.mark.parametrize(
    "n,expected",
    [
        (11, 15),
        (8, 9),
        (10, 12),
        (1, 1),
    ],
)
def test_nthUglyNumber(n, expected):
    assert Solution().nthUglyNumber(n) == expected
