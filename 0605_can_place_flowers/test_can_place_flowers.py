import pytest


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        def can_place(i):
            left_flower = flowerbed[i - 1] if i > 0 else None
            right_flower = flowerbed[i + 1] if i < len(flowerbed) - 1 else None

            if left_flower in [0, None] and right_flower in [0, None]:
                return True
            return False

        for index in range(len(flowerbed)):
            if flowerbed[index] == 0:
                if can_place(index):
                    flowerbed[index] = 1
                    n -= 1
            if n == 0:
                return True

        return False


@pytest.mark.parametrize(
    "flowerbed,n,expected",
    [
        ([0, 0, 0, 0, 0, 1, 0, 0], 0, True),
        ([1, 0, 0, 0, 1, 0, 0], 2, True),
        ([0, 0, 1, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
    ],
)
def test_canPlaceFlowers(flowerbed: list[int], n: int, expected: bool):
    assert Solution().canPlaceFlowers(flowerbed, n) == expected
