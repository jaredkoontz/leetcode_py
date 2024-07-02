import pytest


class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        return self.threeConsecutiveOdds_smarter(arr)

    @staticmethod
    def threeConsecutiveOdds_smarter(arr: list[int]) -> bool:
        if len(arr) < 2:
            return False

        for index in range(2, len(arr)):
            curr = arr[index - 2]
            next_1 = arr[index - 1]
            next_2 = arr[index]

            if curr % 2 == 1 and next_1 % 2 == 1 and next_2 % 2 == 1:
                return True

        return False

    @staticmethod
    def threeConsecutiveOdds_iter(arr: list[int]) -> bool:
        three_in_a_row = 0
        for num in arr:
            if num & 1 == 1:
                three_in_a_row += 1
            else:
                three_in_a_row = 0

            if three_in_a_row == 3:
                return True

        return False


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([2, 6, 4, 1], False),
        ([1, 2, 34, 3, 4, 5, 7, 23, 12], True),
    ],
)
def test_threeConsecutiveOdds(arr, expected):
    assert Solution().threeConsecutiveOdds(arr) == expected
