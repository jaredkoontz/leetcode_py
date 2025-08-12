# https://leetcode.com/problems/fizz-buzz
import pytest


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        return self.fizzBuzz_mine(n)

    @staticmethod
    def fizzBuzz_mine(n: int) -> list[str]:
        ret = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ret.append("FizzBuzz")

            elif i % 3 == 0:
                ret.append("Fizz")
            elif i % 5 == 0:
                ret.append("Buzz")
            else:
                ret.append(f"{i}")
        return ret


@pytest.mark.parametrize(
    "n, expected",
    [
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (
                15,
                [
                    "1",
                    "2",
                    "Fizz",
                    "4",
                    "Buzz",
                    "Fizz",
                    "7",
                    "8",
                    "Fizz",
                    "Buzz",
                    "11",
                    "Fizz",
                    "13",
                    "14",
                    "FizzBuzz",
                ],
        ),
    ],
)
def test_fizzbuzz(n, expected):
    assert Solution().fizzBuzz(n) == expected
