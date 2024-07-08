import pytest


def get_josephus(n: int) -> int:
    # Get the highest power of 2 less than or equal to n
    highest_power_of_2 = 1
    while highest_power_of_2 <= n:
        highest_power_of_2 <<= 1
    highest_power_of_2 >>= 1

    # Calculate the position of the last remaining person
    left_over = n - highest_power_of_2
    return (2 * left_over) + 1


@pytest.mark.parametrize(
    "n,expected", [(1, 1), (2, 1), (3, 3), (4, 1), (5, 3), (12, 9), (41, 19)]
)
def test_josephus(n: int, expected) -> None:
    assert get_josephus(n) == expected
