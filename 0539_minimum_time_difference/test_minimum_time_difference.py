# https://leetcode.com/problems/minimum-time-difference
import pytest


class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        return self.findMinDifference_bucket_sort(timePoints)

    @staticmethod
    def findMinDifference_bucket_sort(timePoints: list[str]) -> int:
        # create buckets array for the times converted to all_minutes
        minutes_in_day = 24 * 60
        all_minutes = [False] * minutes_in_day
        for time in timePoints:
            hours, minute = map(int, time.split(":"))
            time_in_minutes = (hours * 60) + minute
            if all_minutes[time_in_minutes]:
                return 0
            all_minutes[time_in_minutes] = True

        prev_index = float("inf")
        first_index = float("inf")
        last_index = float("inf")
        ans = float("inf")

        # find differences between adjacent elements in sorted array
        for i in range(minutes_in_day):
            if all_minutes[i]:
                if prev_index != float("inf"):
                    ans = min(ans, i - prev_index)
                prev_index = i
                if first_index == float("inf"):
                    first_index = i
                last_index = i

        return min(ans, minutes_in_day - last_index + first_index)

    @staticmethod
    def findMinDifference_concise_sort(timePoints: list[str]) -> int:
        # You can also add the first element plus 24 * 60 to the end of the array
        # It would give the same difference as manually comparing the last and first element.
        time_points = sorted(int(time[:2]) * 60 + int(time[3:]) for time in timePoints)
        time_points.append(24 * 60 + time_points[0])
        return min(
            time_points[i] - time_points[i - 1] for i in range(1, len(time_points))
        )

    @staticmethod
    def findMinDifference_regular_sort(timePoints: list[str]) -> int:
        def total_minutes(hour: int, minute: int) -> int:
            return (hour * 60) + minute

        min_distance = float("inf")
        all_minutes = []
        minutes_in_day = 24 * 60
        for time in timePoints:
            time = time.split(":")
            all_minutes.append(total_minutes(int(time[0]), int(time[1])))
        all_minutes.sort()
        for i in range(len(all_minutes) - 1):
            time1 = all_minutes[i]
            time2 = all_minutes[i + 1]
            distance = time2 - time1
            min_distance = min(distance, min_distance)
            if min_distance == 0:
                return 0

        # look at first and last element
        min_distance = min(
            min_distance, minutes_in_day - (all_minutes[-1] + all_minutes[0])
        )
        return min_distance


@pytest.mark.parametrize(
    "timePoints,expected",
    [
        (["23:59", "00:00"], 1),
        (["00:59", "00:00"], 59),
        (["00:00", "23:59", "00:00"], 0),
        (["05:00", "11:00", "07:34", "07:00", "11:30"], 30),
    ],
)
def test_findMinDifference(timePoints, expected):
    assert Solution().findMinDifference(timePoints) == expected
