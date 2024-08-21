# https://leetcode.com/problems/boats-to-save-people
import pytest


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        return self.numRescueBoats_bucket(people, limit)

    @staticmethod
    def numRescueBoats_bucket(people: list[int], limit: int) -> int:
        # Create an array (bucket) to count occurrences of each weight
        buckets = [0] * (limit + 1)

        # Fill the buckets with the counts of people with each weight
        for p in people:
            buckets[p] += 1

        start = 0
        end = limit
        boats = 0

        while start <= end:
            # Ensure 'start' points to a valid bucket with people
            while start <= end and buckets[start] <= 0:
                start += 1

            # Ensure 'end' points to a valid bucket with people
            while start <= end and buckets[end] <= 0:
                end -= 1

            if buckets[start] <= 0 and buckets[end] <= 0:
                break  # If no valid people left, break the loop

            boats += 1  # Need a new boat

            # If the combined weight of the lightest and heaviest people is within the limit
            if start + end <= limit:
                buckets[start] -= 1

            buckets[end] -= 1

        return boats

    @staticmethod
    def numRescueBoats_two_pointer(people: list[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people) - 1
        boats = 0

        while start <= end:
            boats += 1
            if start == end:  # If there's only one person left
                break

            if people[start] + people[end] <= limit:
                start += 1
            end -= 1

        return boats


@pytest.mark.parametrize(
    "people,limit,expected",
    [
        ([1, 2], 3, 1),
        ([3, 2, 2, 1], 3, 3),
        ([3, 5, 3, 4], 5, 4),
        ([3, 5, 3, 4], 6, 3),
        ([3, 5, 3, 4], 7, 3),
    ],
)
def test_numRescueBoats(people, limit, expected):
    assert Solution().numRescueBoats(people, limit) == expected
