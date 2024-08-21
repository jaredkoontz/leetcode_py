# https://leetcode.com/problems/number-of-changing-keys
import pytest


class Solution:
    @staticmethod
    def countKeyChanges(s: str) -> int:
        changed = 0
        if s:
            curr_key = s[0].lower()
            for i in range(1, len(s)):
                if s[i].lower() != curr_key:
                    changed += 1
                    curr_key = s[i].lower()

        return changed


@pytest.mark.parametrize(
    "s,expected",
    [
        ("aAbBcC", 2),
        ("AaAaAaaA", 0),
        ("aBbCcDd", 3),
        ("aBbCcccDDDDcd", 5),
        ("abbacdbad", 7),
        ("", 0),
    ],
)
def test_count_key_changes(s, expected):
    assert Solution().countKeyChanges(s) == expected
