# https://leetcode.com/problems/implement-trie-prefix-tree
import pytest

from helpers import trie

Trie = trie.Trie


@pytest.mark.parametrize(
    "operations, init, expected",
    [
        (
                ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
                [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
                [None, None, True, False, True, None, True],
        ),
    ],
)
def test_custom_stack(operations, init, expected):
    my_trie = None
    for op, components, curr_val in zip(operations, init, expected):
        if op == "Trie":
            my_trie = Trie()
        elif op == "insert":
            assert my_trie.insert(components[0]) == curr_val
        elif op == "search":
            assert my_trie.search(components[0]) == curr_val
        else:
            assert my_trie.startsWith(components[0]) == curr_val
