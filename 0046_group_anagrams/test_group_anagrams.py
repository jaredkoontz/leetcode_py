import pytest

from helpers.test_helpers import compare_lists


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        str_map = {}
        for string in strs:
            ch_list = [0] * 26
            for ch in string:
                ch_list[ord(ch) - ord("a")] += 1
            hashable = tuple(ch_list)
            if str_map.get(hashable):
                str_map[hashable].append(string)
            else:
                str_map[hashable] = [string]
        ret = []
        for hashable in str_map:
            ret.append(str_map[hashable])
        return ret


@pytest.mark.parametrize(
    "strs,expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_group_anagrams(strs: list[str], expected: list[list[str]]):
    assert compare_lists(Solution().groupAnagrams(strs), expected)
