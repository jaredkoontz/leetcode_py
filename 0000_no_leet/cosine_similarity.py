# Time:  O(n)
# Space: O(1)
from math import sqrt

import pytest


def cosineSimilarity(A, B):
    invalid = 2.0
    if len(A) != len(B):
        return invalid
    A_dot_B, A_dot_A, B_dot_B = 0.0, 0.0, 0.0
    for i in range(len(A)):
        A_dot_B += A[i] * B[i]
        A_dot_A += A[i] * A[i]
        B_dot_B += B[i] * B[i]
    return A_dot_B / sqrt(A_dot_A) / sqrt(B_dot_B) if A_dot_A and B_dot_B else invalid


@pytest.mark.parametrize(
    "A,B,expected",
    [
        ([0], [0], 2),
    ],
)
def test_cosineSimilarity(A, B, expected):
    assert cosineSimilarity(A, B) == expected
