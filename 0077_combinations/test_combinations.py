import pytest


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return self.combine_backtrack(n, k)

    @staticmethod
    def combine_backtrack(n: int, k: int) -> list[list[int]]:
        ret = []
        choices = [x for x in range(1, n + 1)]

        def dfs(index, curr):
            if len(curr) == k:
                ret.append(curr[:])
                return
            if index >= n:
                return

            # choose index
            curr.append(choices[index])
            dfs(index + 1, curr)
            curr.pop()

            # don't choose index
            dfs(index + 1, curr)

            return

        dfs(0, [])
        return ret


@pytest.mark.parametrize(
    "n,k,expected",
    [
        (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
        (1, 1, [[1]]),
    ],
)
def test_combine(n, k, expected):
    assert Solution().combine(n, k) == expected
