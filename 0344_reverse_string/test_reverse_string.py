import pytest


class Solution:
    def reverseString(self, s: list[str]) -> None:
        self.reverseString_mine(s)

    @staticmethod
    def reverseString_mine(s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]

    @staticmethod
    def reverseString_two_pointer(s: list[str]) -> None:
        r = list(s)
        i, j = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

    def reverseString_python(self, s: list[str]) -> None:
        s = s[::-1]

    def reverseString_recursive(self, s: list[str]) -> list[str]:
        n = len(s)
        if n < 2:
            return s
        return self.reverseString_recursive(s[n / 2 :]) + self.reverseString_recursive(
            s[: n / 2]
        )


@pytest.mark.parametrize(
    "s, expected",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ],
)
def test_reverseString(s, expected):
    Solution().reverseString(s)
    assert s == expected
