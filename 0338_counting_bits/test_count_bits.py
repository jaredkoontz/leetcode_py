import pytest


class Solution:
    def countBits(self, n: int) -> list[int]:
        return self.countBits_mine(n)

    @staticmethod
    def countBits_mine(n: int) -> list[int]:
        counter = [0]
        for i in range(1, n + 1):
            counter.append(counter[i >> 1] + i % 2)
            # count also do counter[i//2] + (i & 1)
        return counter

    @staticmethod
    def countBits_bin_count(n: int) -> list[int]:
        return [bin(i).count("1") for i in range(n + 1)]

    @staticmethod
    def countBits_tracker(n: int) -> list[int]:
        next_order = 2
        tracker = 0
        counter = [0] * (n + 1)

        for i in range(1, n + 1):
            if i == next_order:
                # multiply by two
                next_order <<= 1
                tracker = 0
            counter[i] = counter[tracker] + 1
            tracker += 1
        return counter


@pytest.mark.parametrize(
    "n,expected",
    [
        (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
    ],
)
def test_count_bits(n, expected):
    assert Solution().countBits(n) == expected
