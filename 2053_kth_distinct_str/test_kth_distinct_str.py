# https://leetcode.com/problems/kth-distinct-string-in-an-array
import pytest


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        return self.kthDistinct_one_set(arr, k)

    @staticmethod
    def kthDistinct_one_set(arr: list[str], k: int) -> str:
        frequency_map = {}

        # First pass: Populate the frequency map
        for s in arr:
            frequency_map[s] = frequency_map.get(s, 0) + 1

        # Second pass: Find the k-th distinct string
        for s in arr:
            # Check if the current string is distinct
            if frequency_map[s] == 1:
                k -= 1
            # When k reaches 0, we have found the k-th distinct string
            if k == 0:
                return s

        return ""

    @staticmethod
    def kthDistinct_two_sets(arr: list[str], k: int) -> str:
        distinct = {}
        not_distinct = set()
        for val in arr:
            if val not in distinct and val not in not_distinct:
                distinct[val] = ""
            else:
                try:
                    distinct.pop(val)
                except KeyError:
                    pass
                not_distinct.add(val)

        for index, val in enumerate(distinct.keys()):
            if index == k - 1:
                return val
        return ""


@pytest.mark.parametrize(
    "arr,k,expected",
    [
        (
                [
                    "c",
                    "exjk",
                    "nbmg",
                    "kgnas",
                    "s",
                    "oydx",
                    "ghpao",
                    "c",
                    "r",
                    "ohdm",
                    "fq",
                    "ashgg",
                    "mm",
                    "cc",
                    "mymy",
                    "w",
                    "t",
                    "neb",
                    "grjdb",
                    "cukk",
                    "ujyhn",
                    "dq",
                    "hhuo",
                    "qu",
                    "seslw",
                    "ybulz",
                    "iug",
                    "rs",
                    "kyfu",
                    "krz",
                    "nw",
                    "txnn",
                    "r",
                    "zpuao",
                    "sh",
                    "rfc",
                    "c",
                    "hgr",
                    "jfia",
                    "egm",
                    "gmuuv",
                    "gh",
                    "x",
                    "nfvgv",
                    "ibo",
                    "al",
                    "wn",
                    "o",
                    "dyu",
                    "zgkk",
                    "gdzrf",
                    "m",
                    "ui",
                    "xwsj",
                    "zeld",
                    "muowr",
                    "d",
                    "xgiu",
                    "yfu",
                ],
                19,
                "dq",
        ),
        (["d", "b", "c", "b", "c", "a"], 2, "a"),
        (["aaa", "aa", "a"], 1, "aaa"),
        (["a", "b", "a"], 3, ""),
    ],
)
def test_kth_distinct(arr, k, expected):
    assert Solution().kthDistinct(arr, k) == expected
