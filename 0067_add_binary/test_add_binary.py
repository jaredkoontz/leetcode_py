import pytest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return self.addBinary_mine(a, b)

    @staticmethod
    def addBinary_optimal(a: str, b: str) -> str:
        carry = 0
        result = ""

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry % 2)
            carry //= 2

        return result[::-1]

    @staticmethod
    def addBinary_mine(a: str, b: str) -> str:
        diff = abs(len(a) - len(b))
        a = "0" * diff * (len(a) < len(b)) + a
        b = "0" * diff * (len(b) < len(a)) + b
        ret = []
        carry = 0
        for i, c in zip(reversed(a), reversed(b)):
            bit1, bit2 = int(i), int(c)
            curr_bit = (bit1 + bit2 + carry) % 2
            carry = (bit1 + bit2 + carry) // 2
            ret.append(str(curr_bit))
        if carry:  # if carry remain
            ret.append(str(carry))
        return "".join(reversed(ret))


@pytest.mark.parametrize(
    "b1,b2,expected",
    [
        ("0", "1", "1"),
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        ("1", "1", "10"),
    ],
)
def test_add(b1, b2, expected):
    assert Solution().addBinary(b1, b2) == expected
