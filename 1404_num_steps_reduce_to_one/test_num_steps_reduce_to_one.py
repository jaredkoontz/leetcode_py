import pytest


class Solution:
    def numSteps(self, s: str) -> int:
        return self.numSteps_bit(s)

    @staticmethod
    def numSteps_reverse(s: str) -> int:
        res = 0
        carry = 0

        for i in reversed(range(1, len(s))):
            digit = (int(s[i]) + carry) % 2
            if digit == 0:
                res += 1
            else:
                carry = 1
                res += 2

        return res + carry

    @staticmethod
    def numSteps_arr(s: str) -> int:
        s_len = len(s) - 1
        carry = 0
        count = 0
        while s_len > 0:
            # even number with carry = 0, result even
            if int(s[s_len]) + carry == 0:
                carry = 0
                count += 1
            # odd number with carry = 1, result even
            elif int(s[s_len]) + carry == 2:
                carry = 1
                count += 1
            # even number with carry = 1, result odd
            # odd number with carry = 0, result odd
            else:
                carry = 1
                count += 2
            s_len -= 1
        # last digit 1 needs to add a carried over digit 1, which gives 10.
        # So need one more divide to make it 1 (one more step)
        if carry == 1:
            count += 1
        return count

    @staticmethod
    def numSteps_bit(s: str) -> int:
        value = int(s, 2)
        steps = 0
        while value != 1:
            if value & 1:
                value += 1
            else:
                # value //= 2
                value >>= 1
            steps += 1
        return steps


@pytest.mark.parametrize(
    "s,expected",
    [
        ("1111011110000011100000110001011011110010111001010111110001", 85),
        ("1101", 6),
        ("10", 1),
        ("1", 0),
    ],
)
def test_num_steps_reduce_to_one(s, expected):
    assert Solution().numSteps(s) == expected
