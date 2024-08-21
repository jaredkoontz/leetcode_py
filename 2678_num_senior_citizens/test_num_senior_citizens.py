# https://leetcode.com/problems/number-of-senior-citizens
import pytest


class Solution:
    def countSeniors(self, details: list[str]) -> int:
        return self.countSeniors_mine(details)

    @staticmethod
    def countSeniors_mine(details: list[str]) -> int:
        count = 0
        for detail in details:
            age = int(detail[-4:-2])
            if age > 60:
                count += 1
        return count


@pytest.mark.parametrize(
    "details,expected",
    [
        (["7868190130M7522", "5303914400F9211", "9273338290F4010"], 2),
        (["1313579440F2036", "2921522980M5644"], 0),
    ],
)
def test_countSeniors(details, expected):
    assert Solution().countSeniors(details) == expected
