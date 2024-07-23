import pytest


class Solution:
    def decodeString(self, s: str) -> str:
        return self.decodeString_rec(s)

    @staticmethod
    def decodeString_rec(s: str) -> str:
        def dfs(i):
            stack = []
            num = 0
            while i < len(s):
                if s[i] == "[":
                    (j, out) = dfs(i + 1)
                    stack.append(num * out)
                    i = j
                    num = 0
                elif s[i] == "]":
                    return i, "".join(stack)
                elif "0" <= s[i] <= "9":
                    num *= 10
                    num += int(s[i])
                else:
                    stack.append(s[i])
                i += 1
            return "".join(stack)

        final: str = dfs(0)
        return final

    @staticmethod
    def decodeString_stack(s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = ""
        for c in s:
            if c == "[":
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ""
                cur_num = 0
            elif c == "]":
                num = stack.pop()
                prev_str = stack.pop()
                cur_str = prev_str + num * cur_str
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                cur_str += c
        return cur_str


@pytest.mark.parametrize(
    "s,expected",
    [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ],
)
def test_decodeString(s, expected):
    assert Solution().decodeString(s) == expected
