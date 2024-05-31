import pytest


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        my_list = []
        cost, left, max_len = 0, 0, 0
        for s_ch, t_ch in zip(s, t):
            s_cost = ord("a") - ord(s_ch)
            t_cost = ord("a") - ord(t_ch)
            my_list.append(abs(s_cost - t_cost))
        # sliding window
        for right in range(len(my_list)):
            cost += my_list[right]
            while cost > maxCost:
                cost -= my_list[left]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len


@pytest.mark.parametrize(
    "s,t,max_cost,expected",
    [
        ("abcd", "bcdf", 3, 3),
        ("abcd", "cdef", 3, 1),
        ("abcd", "acde", 0, 1),
        ("krrgw", "zjxss", 19, 2),
    ],
)
def test_equalSubstring(s, t, max_cost, expected):
    assert Solution().equalSubstring_learning(s, t, max_cost) == expected
