from collections import defaultdict

import pytest


class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        return self.countDays_merge_intervals(days, meetings)

    @staticmethod
    def countDays_sweep(days: int, meetings: list[list[int]]) -> int:
        day_map = defaultdict(int)

        for start, end in meetings:
            day_map[start] += 1
            day_map[end + 1] -= 1

        sorted_days = sorted(day_map.items())
        ans = 0

        if sorted_days:
            first_day = sorted_days[0][0]
            ans += first_day - 1  # Days before first meeting start

        cum_sum = 0
        for i in range(1, len(sorted_days)):
            prev_day, _ = sorted_days[i - 1]
            curr_day, delta = sorted_days[i]

            cum_sum += day_map[prev_day]

            if cum_sum == 0:
                gap_end = min(curr_day, days + 1)
                ans += gap_end - prev_day

        # Final check for last segment
        cum_sum += day_map[sorted_days[-1][0]]
        if cum_sum == 0 and sorted_days[-1][0] <= days:
            ans += days - sorted_days[-1][0] + 1

        return ans

    @staticmethod
    def countDays_merge_intervals(days: int, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        count = meetings[0][0] - 1
        n = len(meetings)
        for i in range(1, n):
            if meetings[i][0] <= meetings[i - 1][1]:
                if meetings[i][1] < meetings[i - 1][1]:
                    meetings[i][1] = meetings[i - 1][1]
            else:
                dy = meetings[i][0] - meetings[i - 1][1]
                count += dy - 1
        count += days - meetings[n - 1][1]
        return count

    @staticmethod
    def countDays_naive(days: int, meetings: list[list[int]]) -> int:
        if not meetings:
            return days
        avail = set(x for x in range(1, days + 1))
        for entry_range in meetings:
            start_date = entry_range[0]
            end_date = entry_range[1] + 1
            for i in range(start_date, end_date):
                try:
                    avail.remove(i)
                except KeyError:
                    # a meeting when we are not working, or an already recorded meeting,
                    # simple ignore and move on
                    pass

        return len(avail)


@pytest.mark.parametrize(
    "days,meetings,expected",
    [
        (10, [[5, 7], [1, 3], [9, 10]], 2),
        (5, [[2, 4], [1, 3]], 1),
        (6, [[1, 6]], 0),
    ],
)
def test_countDays(days, meetings, expected):
    assert Solution().countDays(days, meetings) == expected
