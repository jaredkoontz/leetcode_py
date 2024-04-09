import pytest

PHONE_MAPPING = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        return self.letterCombinations_mine(digits)

    @staticmethod
    def letterCombinations_mine(digits: str) -> list[str]:
        res = []

        def backtrack(index, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for c in PHONE_MAPPING[digits[index]]:
                backtrack(index + 1, curr + c)

        if digits:
            backtrack(0, "")
        return res

    @staticmethod
    def letterCombinations_backtrack(digits: str) -> list[str]:
        res = []

        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return

            for letter in PHONE_MAPPING[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

        if digits:
            backtrack("", digits)
        return res

    @staticmethod
    def letterCombinations_dfs(digits: str) -> list[str]:
        result = []
        if len(digits) == 0:
            return result

        def dfs(nums, index, path, res):
            if index >= len(nums):
                res.append(path)
                return
            string1 = PHONE_MAPPING[nums[index]]
            for i in string1:
                dfs(nums, index + 1, path + i, res)

        dfs(digits, 0, "", result)
        return result


@pytest.mark.parametrize(
    "digits, expected",
    [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
        ("58", ["jt", "ju", "jv", "kt", "ku", "kv", "lt", "lu", "lv"]),
        (
            "92",
            ["wa", "wb", "wc", "xa", "xb", "xc", "ya", "yb", "yc", "za", "zb", "zc"],
        ),
        ("65", ["mj", "mk", "ml", "nj", "nk", "nl", "oj", "ok", "ol"]),
        (
            "78",
            ["pt", "pu", "pv", "qt", "qu", "qv", "rt", "ru", "rv", "st", "su", "sv"],
        ),
    ],
)
def test_letterCombinations(digits, expected):
    assert Solution().letterCombinations(digits) == expected
