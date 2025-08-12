# https://leetcode.com/problems/repeated-dna-sequences
import pytest

from helpers.testing_helpers import compare_flat_lists


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        return self.findRepeatedDnaSequences_two_set(s)

    @staticmethod
    def findRepeatedDnaSequences_two_set(s: str) -> list[str]:
        ans, seen = set(), set()
        for i in range(len(s) - 9):
            dna = s[i : i + 10]
            if dna in seen:
                ans.add(dna)
            else:
                seen.add(dna)
        return list(ans)

    @staticmethod
    def findRepeatedDnaSequences_mine(s: str) -> list[str]:
        ret = []
        all_combos = {}
        for index in range(len(s)):
            end_index = index + 10
            if end_index >= len(s):
                break
            new_str = s[index:end_index]
            if new_str not in all_combos:
                all_combos[new_str] = 1
            else:
                all_combos[new_str] += 1

        for key, appears in all_combos.items():
            if appears > 1:
                ret.append(key)

        return ret


@pytest.mark.parametrize(
    "s, expected",
    [
        ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["CCCCCAAAAA", "AAAAACCCCC"]),
        ("AAAAAAAAAAAAA", ["AAAAAAAAAA"]),
    ],
)
def test_findRepeatedDnaSequences(s, expected):
    assert compare_flat_lists(Solution().findRepeatedDnaSequences(s), expected)
