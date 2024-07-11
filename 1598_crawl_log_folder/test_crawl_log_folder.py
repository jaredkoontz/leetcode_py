import pytest


class Solution:
    def minOperations(self, logs: list[str]) -> int:
        return self.minOperations_mine(logs)

    def minOperations_mine(self, logs: list[str]) -> int:
        stack = []
        for log in logs:
            if log == "./":
                ...
            elif log == "../":
                if stack:
                    stack.pop()
            else:
                stack.append(log)
        print(stack)
        return len(stack)


@pytest.mark.parametrize(
    "logs,expected",
    [
        (["d1/", "d2/", "../", "d21/", "./"], 2),
        (["d1/", "d2/", "./", "d3/", "../", "d31/"], 3),
        (["d1/", "../", "../", "../"], 0),
    ],
)
def test_minOperations(logs, expected):
    assert Solution().minOperations(logs) == expected
