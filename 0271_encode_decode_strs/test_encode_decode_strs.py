import pytest


class Solution:
    DELIMITER = "#"

    def encode(self, strs: list[str]) -> str:
        my_str = ""
        for s in strs:
            my_str += f"{len(s)}{self.DELIMITER}{s}"
        return my_str

    def decode(self, s: str) -> list[str]:
        my_list = []
        index = 0

        while index < len(s) - 1:
            j = index
            while s[j] != self.DELIMITER:
                j += 1
            length = int(s[index:j])
            index = j + 1
            my_list.append(s[index: index + length])
            index += length
        return my_list


@pytest.mark.parametrize(
    "l1,expected",
    [
        (["neet", "code", "love", "you"], ["neet", "code", "love", "you"]),
        (
                ["#4neet", "#4code", "#4love", "#3you"],
                ["#4neet", "#4code", "#4love", "#3you"],
        ),
        (["we", "say", ":", "yes"], ["we", "say", ":", "yes"]),
        (
                ["2#we", "3say", "1:", "5yes"],
                ["2#we", "3say", "1:", "5yes"],
        ),
        (
                ["we", "say", ":", "yes", "!@#$%^&*()"],
                ["we", "say", ":", "yes", "!@#$%^&*()"],
        ),
    ],
)
def test_encode_decode(l1, expected):
    assert Solution().decode(Solution().encode(l1)) == expected
