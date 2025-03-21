# https://leetcode.com/problems/search-suggestions-system
import collections
import heapq

import pytest

from helpers.trie import add_to_trie
from helpers.trie import traverse_trie_from_term
from helpers.trie import TrieNode


class Solution:
    def suggestedProducts(
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        return self.suggestedProducts_trie(products, searchWord)

    @staticmethod
    def suggestedProducts_sort(products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        ans = []
        left, right = 0, len(products) - 1

        for i in range(len(searchWord)):
            c = searchWord[i]
            res = []

            while left <= right and (len(products[left]) <= i or products[left][i] < c):
                left += 1
            while left <= right and (
                len(products[right]) <= i or products[right][i] > c
            ):
                right -= 1

            for j in range(3):
                if left + j <= right:
                    res.append(products[left + j])
            ans.append(res)

        return ans

    @staticmethod
    def suggestedProducts_trie_heap(
        products: list[str], searchWord: str
    ) -> list[list[str]]:
        class LocalTrieNode:
            def __init__(self):
                self.children = collections.defaultdict(LocalTrieNode)
                self.h = []

            def add_sugesstion(self, product):
                if len(self.h) < 3:
                    heapq.heappush(self.h, MaxHeapStr(product))
                else:
                    heapq.heappushpop(self.h, MaxHeapStr(product))

            def get_suggestion(self):
                return sorted(self.h, reverse=True)

        class MaxHeapStr(str):
            def __init__(self, string):
                self.string = string

            def __lt__(self, other):
                return self.string > other.string

            def __eq__(self, other):
                return self.string == other.string

        root = LocalTrieNode()
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add_sugesstion(p)

        result, node = [], root
        for char in searchWord:
            node = node.children[char]
            result.append(node.get_suggestion())
        return result

    @staticmethod
    def suggestedProducts_trie_sort(
        products: list[str], searchWord: str
    ) -> list[list[str]]:
        class LocalTrieNode:
            def __init__(self):
                self.children = collections.defaultdict(LocalTrieNode)
                self.suggestion = []

            def add_suggestion(self, product):
                if len(self.suggestion) < 3:
                    self.suggestion.append(product)

        products = sorted(products)
        root = LocalTrieNode()
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add_suggestion(p)

        result, node = [], root
        for char in searchWord:
            node = node.children[char]
            result.append(node.suggestion)
        return result

    @staticmethod
    def suggestedProducts_trie(products: list[str], searchWord: str) -> list[list[str]]:
        suggested = []
        root = TrieNode()
        for product in products:
            add_to_trie(root, product)

        search_term = ""
        for char in searchWord:
            search_term += char
            suggested.append(traverse_trie_from_term(root, search_term))

        return suggested


@pytest.mark.parametrize(
    "products,searchWord,expected",
    [
        (
            ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
            "mouse",
            [
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
        ),
        (
            ["havana"],
            "havana",
            [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]],
        ),
    ],
)
def test_suggestedProducts(products, searchWord, expected):
    assert Solution().suggestedProducts(products, searchWord) == expected
