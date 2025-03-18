# Time:  O(n*m)
# Space: O(m)
#
# Given n items with size A[i], an integer m denotes the size of a backpack.
# How full you can fill this backpack?
#
# Note
# You can not divide any item into small pieces.
#
# Example
# If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can select 2, 3 and 5,
# so that the max size we can fill this backpack is 10. If the backpack size is 12.
# we can select [2, 3, 7] so that we can fulfill the backpack.
#
# Your function should return the max size we can fill in the given backpack.
#
# @param m: An integer m denotes the size of a backpack
# @param A: Given n items with size A[i]
# @return: The maximum size
import pytest


def backPack(m, A):
    d = [[False for j in range(m + 1)] for i in range(2)]
    result = 0
    d[0][0] = True

    for i in range(1, len(A) + 1):
        d[i % 2][0] = True
        for j in range(1, m + 1):
            d[i % 2][j] = d[(i - 1) % 2][j]
            if j >= A[i - 1]:
                d[i % 2][j] = d[(i - 1) % 2][j] or d[(i - 1) % 2][j - A[i - 1]]
            if d[i % 2][j]:
                result = max(result, j)

    return result


@pytest.mark.parametrize(
    "m,A,expected",
    [
        (11, [2, 3, 5, 7], 10),
        (12, [2, 3, 5, 7], 12),
    ],
)
def test_backPack(m, A, expected):
    assert backPack(m, A) == expected
