import pytest

MAPPINGS = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        return self.romanToInt_theirs(s)

    @staticmethod
    def romanToInt_theirs(s: str) -> int:
        total = 0
        for i in range(len(s)):
            curr = s[i]
            next_one = s[i + 1] if i + 1 < len(s) else 0

            if MAPPINGS[curr] < MAPPINGS.get(next_one, 0):
                total -= MAPPINGS[curr]
            else:
                total += MAPPINGS[curr]

        return total

    @staticmethod
    def romanToInt_mine(s: str) -> int:
        total = 0

        for index in range(len(s)):
            curr_value = MAPPINGS[s[index]]
            next_index = index + 1
            if next_index < len(s):
                next_char = s[next_index]
                next_char_value = MAPPINGS[next_char]
                if next_char_value > curr_value:
                    total -= curr_value
                else:
                    total += curr_value
            else:
                total += curr_value
        return total


@pytest.mark.parametrize(
    "roman,expected",
    [
        ("III", 3),
        ("LVIII", 58),
        ("IV", 4),
        ("XL", 40),
        ("IX", 9),
        ("MCM", 1900),
        ("MCMXCIV", 1994),
        ("MCMXC", 1990),
    ],
)
def test_romanToInt(roman, expected):
    assert Solution().romanToInt(roman) == expected
