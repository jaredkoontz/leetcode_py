import pytest

from helpers.test_helpers import compare_nested_lists


def groupIsomorphic(strs: list[str]) -> list[list[str]]:
    return groupIsomorphic_naive(strs)


def groupIsomorphic_naive(strs: list[str]) -> list[list[str]]:
    def isIsomorphic(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map, t_map = {}, {}
        for s_char, t_char in zip(s, t):
            if (s_char in s_map and s_map[s_char] != t_char) or (
                t_char in t_map and t_map[t_char] != s_char
            ):
                return False
            s_map[s_char], t_map[t_char] = t_char, s_char
        return True

    structures = {strs[0]: [strs[0]]}
    for i in range(1, len(strs)):
        s = strs[i]
        found = False
        for key in structures:
            if isIsomorphic(s, key):
                structures[key].append(s)
                found = True
                break
        if not found:
            structures[s] = [s]

    res = []
    for key in structures:
        res.append(structures[key])
    return res


def groupIsomorphic_encoding(strs: list[str]) -> list[list[str]]:
    def encode(word):
        first_show_dic = {}
        for i, c in enumerate(word):
            if c not in first_show_dic:
                first_show_dic[c] = i
        return tuple([first_show_dic[c] for c in word])

    res = {}
    for s in strs:
        key = encode(s)
        if key not in res:
            res[key] = []
        res[key].append(s)
    return list(res.values())


@pytest.mark.parametrize(
    "l1,expected",
    [
        (
            ["aab", "xxy", "xyz", "abc", "def", "xyx"],
            [["xyx"], ["xyz", "abc", "def"], ["aab", "xxy"]],
        )
    ],
)
def test_groupIsomorphic(l1, expected):
    assert compare_nested_lists(groupIsomorphic(l1), expected)
