import pytest


class Solution:
    def removeStars(self, s: str) -> str:
        return self.removeStars_stack(s)

    @staticmethod
    def removeStars_stack(s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


@pytest.mark.parametrize(
    "s,expected",
    [
        ("leet**cod*e", "lecoe"),
        ("erase*****", ""),
    ],
)
def test_remove_stars_from_str(s, expected):
    assert Solution().removeStars(s) == expected
