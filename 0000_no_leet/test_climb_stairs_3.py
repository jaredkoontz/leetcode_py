import functools

import pytest


"you can either take 1, 2, or 3 steps to reach the top of the stairs, how many ways can we do it."


def climb_stairs_3(n: int) -> int:
    return _climb_stairs_optimal(n)


def _climb_stairs_naive(n: int) -> int:
    def helper(num_steps):
        if num_steps == 0:
            return 1
        if num_steps < 0:
            return 0

        return helper(num_steps - 1) + helper(num_steps - 2) + helper(num_steps - 3)

    return helper(n)


def _climb_stairs_cache(n: int) -> int:
    @functools.cache
    def helper(num_steps):
        if num_steps == 0:
            return 1
        if num_steps < 0:
            return 0

        return helper(num_steps - 1) + helper(num_steps - 2) + helper(num_steps - 3)

    return helper(n)


def _climb_stairs_memo(n: int) -> int:
    if n == 1:
        return 1
    memo = [0] * (n + 1)
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]


def _climb_stairs_optimal(n: int) -> int:
    first = 1
    second = 2
    third = 4

    if n <= 2:
        return n
    if n == 3:
        return third

    for i in range(3, n):
        temp_third = third
        third = first + second + third
        first = second
        second = temp_third
    return third


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),
        (2, 2),
        (3, 4),
        (4, 7),
        (5, 13),
        (6, 24),
        (44, 272_809_183_135),
    ],
)
def test_climb_stairs_3(n, expected):
    assert climb_stairs_3(n) == expected
