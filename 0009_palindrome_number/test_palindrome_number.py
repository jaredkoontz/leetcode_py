import pytest


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return self.isPalindrome_num(x)

    def isPalindrome_num(self, x):
        if x < 0:
            return False

        divider = 1
        while x > 10 * divider:
            divider *= 10

        while x:
            last_num = x % 10
            first_num = x // divider

            if first_num != last_num:
                return False

            x = x % divider
            x = x // 10
            divider = divider // 100

        return True

    def isPalindrome_str(self, x):
        if x < 0:
            return False

        num_str = str(x)
        length = len(num_str) // 2
        for i in range(0, length):
            if num_str[i] != num_str[-i - 1]:
                return False
        return True


@pytest.mark.parametrize(
    "target,expected",
    [
        (121, True),
        (1, True),
        (10, False),
        (100001, True),
        (1321, False),
        (-121, False),
    ],
)
def test_palindrome(target, expected):
    assert Solution().isPalindrome(target) == expected
