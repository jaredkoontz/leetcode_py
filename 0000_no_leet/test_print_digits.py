import pytest


def print_digits_reverse(n):
    ans = []
    while n > 0:
        digit = n % 10
        ans.append(digit)
        n = n // 10
    return ans


def print_digits(n):
    res = []
    while n > 0:
        n, remainder = divmod(n, 10)
        res.insert(0, remainder)
    return res


@pytest.mark.parametrize(
    "n,expected",
    [
        (2, [2]),
        (23, [2, 3]),
        (231, [2, 3, 1]),
        (2310, [2, 3, 1, 0]),
    ],
)
def test_print_digits(n, expected):
    assert print_digits(n) == expected


@pytest.mark.parametrize(
    "n,expected",
    [
        (2, [2]),
        (23, [3, 2]),
        (231, [1, 3, 2]),
        (2310, [0, 1, 3, 2]),
    ],
)
def test_print_digits_reverse(n, expected):
    assert print_digits_reverse(n) == expected
