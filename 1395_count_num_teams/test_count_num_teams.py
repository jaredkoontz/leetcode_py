import pytest


class Solution:
    def numTeams(self, rating: list[int]) -> int:
        return self.numTeams_optimized(rating)

    @staticmethod
    def numTeams_optimized(rating: list[int]) -> int:
        n = len(rating)
        teams = 0

        # Iterate through each soldier as the middle soldier
        for mid in range(n):
            left_smaller = 0
            right_larger = 0

            # Count soldiers with smaller ratings on the left side of the current soldier
            for left in range(mid - 1, -1, -1):
                if rating[left] < rating[mid]:
                    left_smaller += 1

            # Count soldiers with larger ratings on the right side of the current soldier
            for right in range(mid + 1, n):
                if rating[right] > rating[mid]:
                    right_larger += 1

            # Calculate and add the number of ascending rating teams (small-mid-large)
            teams += left_smaller * right_larger

            # Calculate soldiers with larger ratings on the left and smaller ratings on the right
            left_larger = mid - left_smaller
            right_smaller = n - mid - 1 - right_larger

            # Calculate and add the number of descending rating teams (large-mid-small)
            teams += left_larger * right_smaller

        # Return the total number of valid teams
        return teams

    @staticmethod
    def numTeams_tabulation(rating: list[int]) -> int:
        n = len(rating)
        teams = 0

        # Tables for increasing and decreasing sequences
        increasing_teams = [[0] * 4 for _ in range(n)]
        decreasing_teams = [[0] * 4 for _ in range(n)]

        # Fill the base cases. (Each soldier is a sequence of length 1)
        for i in range(n):
            increasing_teams[i][1] = 1
            decreasing_teams[i][1] = 1

        # Fill the tables
        for count in range(2, 4):
            for i in range(n):
                for j in range(i + 1, n):
                    if rating[j] > rating[i]:
                        increasing_teams[j][count] += increasing_teams[i][count - 1]
                    if rating[j] < rating[i]:
                        decreasing_teams[j][count] += decreasing_teams[i][count - 1]

        # Sum up the results (All sequences of length 3)
        for i in range(n):
            teams += increasing_teams[i][3] + decreasing_teams[i][3]

        return teams

    @staticmethod
    def numTeams_memo(rating: list[int]) -> int:
        def _count_increasing_teams(
            my_rating: list[int],
            current_index: int,
            team_size: int,
            increasing_cache: list[list[int]],
        ) -> int:
            n = len(my_rating)

            # Base case: reached end of array
            if current_index == n:
                return 0

            # Base case: found a valid team of size 3
            if team_size == 3:
                return 1

            # Return cached result if available
            if increasing_cache[current_index][team_size] != -1:
                return increasing_cache[current_index][team_size]

            valid_teams = 0

            # Recursively count teams with increasing ratings
            for next_index in range(current_index + 1, n):
                if my_rating[next_index] > my_rating[current_index]:
                    valid_teams += _count_increasing_teams(
                        my_rating, next_index, team_size + 1, increasing_cache
                    )

            # Cache and return the result
            increasing_cache[current_index][team_size] = valid_teams
            return valid_teams

        def _count_decreasing_teams(
            my_rating: list[int],
            current_index: int,
            team_size: int,
            decreasing_cache: list[list[int]],
        ) -> int:
            n = len(my_rating)

            # Base case: reached end of array
            if current_index == n:
                return 0

            # Base case: found a valid team of size 3
            if team_size == 3:
                return 1

            # Return cached result if available
            if decreasing_cache[current_index][team_size] != -1:
                return decreasing_cache[current_index][team_size]

            valid_teams = 0

            # Recursively count teams with decreasing ratings
            for next_index in range(current_index + 1, n):
                if my_rating[next_index] < my_rating[current_index]:
                    valid_teams += _count_decreasing_teams(
                        my_rating, next_index, team_size + 1, decreasing_cache
                    )

            # Cache and return the result
            decreasing_cache[current_index][team_size] = valid_teams
            return valid_teams

        length = len(rating)
        teams = 0
        inc_cache = [[-1] * 4 for _ in range(length)]
        dec_cache = [[-1] * 4 for _ in range(length)]

        # Calculate total teams by considering each soldier as a starting point
        for start_index in range(length):
            teams += _count_increasing_teams(
                rating, start_index, 1, inc_cache
            ) + _count_decreasing_teams(rating, start_index, 1, dec_cache)

        return teams

    @staticmethod
    def numTeams_brute_force(rating: list[int]) -> int:
        num_teams = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                for k in range(j + 1, len(rating)):
                    if (
                        rating[i] < rating[j] < rating[k]
                        or rating[i] > rating[j] > rating[k]
                    ):
                        num_teams += 1
        return num_teams


@pytest.mark.parametrize(
    "rating,expected",
    [
        ([2, 5, 3, 4, 1], 3),
        ([2, 1, 3], 0),
        ([1, 2, 3, 4], 4),
    ],
)
def test_count_num_teams(rating, expected):
    assert Solution().numTeams(rating) == expected
