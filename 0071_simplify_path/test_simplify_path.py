# https://leetcode.com/problems/simplify-path
import pytest


class Solution:
    def simplifyPath(self, path: str) -> str:
        return self.simplifyPath_mine(path)

    @staticmethod
    def simplifyPath_mine(path: str) -> str:
        stack = []
        all_paths = path.split("/")
        for path in all_paths:
            if not path:
                continue

            if path == ".":
                continue

            if path == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(path)
        return f'/{"/".join(stack)}'


@pytest.mark.parametrize(
    "path,expected",
    [
        ("/home/", "/home"),
        ("/home//foo", "/home/foo"),
        ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
        ("/../", "/"),
        ("/../foo", "/foo"),
        ("/.../a/../b/c/../d/./", "/.../b/d"),
        ("/home", "/home"),
        ("/", "/"),
    ],
)
def test_simplify_path(path, expected):
    assert Solution().simplifyPath(path) == expected
