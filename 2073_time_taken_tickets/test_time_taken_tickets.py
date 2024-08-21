# https://leetcode.com/problems/time-needed-to-buy-tickets
import pytest


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        return self.timeRequiredToBuy_clean(tickets, k)

    @staticmethod
    def timeRequiredToBuy_clean(tickets: list[int], k: int) -> int:
        total = 0

        for i in range(len(tickets)):
            if i <= k:
                total += min(tickets[i], tickets[k])
            else:
                total += min(tickets[i], tickets[k] - 1)

        return total

    @staticmethod
    def timeRequiredToBuy_optimized(tickets: list[int], k: int) -> int:
        ans = 0
        for i in range(len(tickets)):
            if i > k:
                if tickets[i] < tickets[k]:
                    ans += tickets[i]
                else:
                    ans += tickets[k] - 1
            else:
                ans += min(tickets[i], tickets[k])

        return ans

    @staticmethod
    def timeRequiredToBuy_first_try(tickets: list[int], k: int) -> int:
        seconds = 0
        while True:
            has_tickets = False
            for i in range(len(tickets)):
                if tickets[i]:
                    tickets[i] -= 1
                    has_tickets = True
                    seconds += 1
                    if i == k:
                        if tickets[i] == 0:
                            break
            if not has_tickets or tickets[k] == 0:
                break
        return seconds


@pytest.mark.parametrize(
    "tickets,k,expected",
    [
        ([2, 3, 2], 2, 6),
        ([5, 1, 1, 1], 0, 8),
        ([84, 49, 5, 24, 70, 77, 87, 8], 3, 154),
        ([3, 4, 6, 5, 2, 7], 3, 23),
    ],
)
def test_time_taken_tickets(tickets: list[int], k: int, expected: int) -> None:
    assert Solution().timeRequiredToBuy(tickets, k) == expected
