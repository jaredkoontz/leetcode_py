from bisect import bisect_left

import pytest

from helpers.trie import TrieNode


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        return self.longestCommonPrefix_trie(arr1, arr2)

    @staticmethod
    def longestCommonPrefix_trie(arr1: list[int], arr2: list[int]) -> int:
        def add_to_trie(node: TrieNode, my_num):
            cur = node
            for ch in str(my_num):
                idx = ord(ch) - ord("0")
                if cur.children.get(idx) is None:
                    cur.children[idx] = TrieNode()
                cur = cur.children[idx]
            cur.end = True

        def prefix_count(node: TrieNode, my_num):
            cur = node
            count = 0
            for ch in str(my_num):
                idx = ord(ch) - ord("0")
                if cur.children.get(idx) is None:
                    return count
                cur = cur.children[idx]
                count += 1
            return count

        root = TrieNode()
        if len(arr2) > len(arr1):
            arr1, arr2 = arr2, arr1

        for num in arr1:
            add_to_trie(root, num)

        max_length = 0
        for num in arr2:
            max_length = max(max_length, prefix_count(root, num))

        return max_length

    @staticmethod
    def longestCommonPrefix_set(arr1: list[int], arr2: list[int]) -> int:
        p_set = set()
        for num in arr1:
            while num > 0:
                p_set.add(num)
                num //= 10

        max_length = 0
        for num in arr2:
            while num > 0:
                length = len(str(num))
                if length <= max_length:
                    break
                if num in p_set:
                    max_length = length
                    break
                num //= 10
        return max_length

    @staticmethod
    def longestCommonPrefix_leet(arr1: list[int], arr2: list[int]) -> int:
        def helper(char_a, char_b):
            if (char_a, char_b) in d:
                return d[(char_a, char_b)]
            if (char_b, char_a) in d:
                return d[(char_b, char_a)]
            count = 0
            for index in range(min(len(char_a), len(char_b))):
                if char_a[index] == char_b[index]:
                    count += 1
                else:
                    break
            d[(char_a, char_b)] = d[(char_b, char_a)] = count
            return count

        ans = 0
        a, b = sorted([str(x) for x in arr1]), [str(x) for x in arr2]
        n = len(a)
        d, d2 = {}, {}
        for i in range(len(b)):
            if (b[i]) in d2:
                idx = d2[b[i]]
            else:
                idx = d2[b[i]] = bisect_left(a, b[i])

            if idx > 0:
                ans = max(ans, helper(a[idx - 1], b[i]))
            if idx < n:
                ans = max(ans, helper(a[idx], b[i]))
        return ans


@pytest.mark.parametrize(
    "arr1,arr2,expected",
    [
        ([1, 10, 100], [1000], 3),
        ([1, 2, 3], [4, 4, 4], 0),
    ],
)
def test_common_prefix(arr1, arr2, expected):
    assert Solution().longestCommonPrefix(arr1, arr2) == expected
