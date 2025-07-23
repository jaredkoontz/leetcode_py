# https://leetcode.com/problems/maximum-score-from-removing-substrings
import re

import pytest


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        return self.maximumGain_greedy(s, x, y)

    @staticmethod
    def maximumGain_backtrack(s: str, x: int, y: int) -> int:
        x_str = "ab"
        y_str = "ba"
        max_score = [0]

        def find(haystack, needle) -> list[int]:
            return [m.start() for m in re.finditer(needle, haystack)]

        def dfs(curr_str, curr_score):
            print(f"{curr_str=}, {curr_score=}")

            max_score[0] = max(max_score[0], curr_score)

            if x_str not in curr_str and y_str not in curr_str:
                return

            for index in find(curr_str, x_str):
                # take the x string away
                dfs(curr_str[:index] + curr_str[index + 2 :], curr_score + x)
            for index in find(curr_str, y_str):
                # take the y string away
                dfs(curr_str[:index] + curr_str[index + 2 :], curr_score + y)

        dfs(s, 0)

        return max_score[0]

    @staticmethod
    def maximumGain_greedy(s: str, x: int, y: int) -> int:
        """
        the key takeaway from the backtrack solution, is that since we have different scores, the optimal
        solution is always going to be greedily taking away the higher point values until we run out of those
        then see if any remaining lower point scores are availble
        """

        def remove_pairs(my_pair, score):
            nonlocal s
            my_res = 0
            stack = []
            for c in s:
                if c == my_pair[1] and stack and stack[-1] == my_pair[0]:
                    stack.pop()
                    my_res += score
                else:
                    stack.append(c)

            s = "".join(stack)
            return my_res

        res = 0
        pair = "ab" if x > y else "ba"

        res += remove_pairs(pair, max(x, y))
        # reverse pair
        res += remove_pairs(pair[::-1], min(x, y))
        return res


@pytest.mark.parametrize(
    "s,x,y,expected",
    [
        ("cdbcbbaaabab", 4, 5, 19),
        ("aabbaaxybbaabb", 5, 4, 20),
    ],
)
def test_maximumGain(s, x, y, expected):
    assert Solution().maximumGain(s, x, y) == expected
