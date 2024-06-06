import pytest


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


def insert(root, word):
    curr = root
    for c in word:
        index = ord(c) - ord("a")
        if curr.children[index] is None:
            curr.children[index] = TrieNode()
        curr = curr.children[index]
    curr.isEndOfWord = True


def search(root, word):
    node = root
    for c in word:
        index = ord(c) - ord("a")
        if node.children[index] is None:
            return False
        node = node.children[index]
    return node.isEndOfWord


def countCommonAnagrams(s1, s2):
    common_anagrams = []
    root = TrieNode()
    n = len(s1)

    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s1[i:j]
            sorted_substr = "".join(sorted(substr))
            insert(root, sorted_substr)

    m = len(s2)

    for i in range(m):
        for j in range(i + 1, m + 1):
            substr = s2[i:j]
            sorted_substr = "".join(sorted(substr))
            if search(root, sorted_substr):
                common_anagrams.append(substr)

    return common_anagrams


@pytest.mark.parametrize(
    "s1,s2,expected",
    [
        ("bca", "abc", ["a", "abc", "b", "bc", "c"]),
        ("ba", "abc", ["a", "ab", "b"]),
    ],
)
def test_common_anagrams(s1, s2, expected):
    assert countCommonAnagrams(s1, s2) == expected
