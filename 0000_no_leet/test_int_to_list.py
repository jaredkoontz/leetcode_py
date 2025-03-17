import pytest

"""
Given an unsigned int, print out each number. If they chose to turn it into a string, ask how we can do it without
strings.

    1 -> 1
    12 -> 1, 2
    107 -> 1, 0 , 7

"""


def int_to_list_loop(number: int) -> list[int]:
    output = []
    curr_place = 10
    if number < 0:
        return []
    else:
        while number > 9:
            digit = number % 10
            number //= curr_place
            output.insert(0, digit)
        output.insert(0, number)

    return output


def int_to_list_rec(number: int) -> list[int]:
    def int_to_list_helper(num, out):
        if num < 10:
            out.append(num)
        else:
            int_to_list_helper(num // 10, out)
            out.append(num % 10)

    if number < 0:
        return []
    output = []
    if number < 10:
        output.append(number)
    else:
        int_to_list_helper(number, output)

    return output


@pytest.mark.parametrize(
    "number,expected",
    [
        (12, [1, 2]),
        (-12, []),
        (1, [1]),
        (8, [8]),
        (10, [1, 0]),
        (107, [1, 0, 7]),
        (100007, [1, 0, 0, 0, 0, 7]),
        (123456789, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ],
)
def test_int_to_list(number: int, expected: list[int]):
    assert int_to_list_loop(number) == expected
    assert int_to_list_rec(number) == expected
