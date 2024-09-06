# https://leetcode.com/problems/group-anagrams
import pytest

from helpers.testing_helpers import freeze_nested_lists


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        return self.groupAnagrams_mine(strs)

    @staticmethod
    def groupAnagrams_mine(strs: list[str]) -> list[list[str]]:
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
        return [x for x in str_map.values()]


@pytest.mark.parametrize(
    "strs,expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["ddddddddddg", "dgggggggggg"], [["ddddddddddg"], ["dgggggggggg"]]),
    ],
)
def test_group_anagrams(strs: list[str], expected: list[list[str]]):
    frozen1, frozen2 = freeze_nested_lists(Solution().groupAnagrams(strs), expected)
    assert frozen1 == frozen2
