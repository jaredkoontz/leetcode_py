import dataclasses


@dataclasses.dataclass
class TrieNode:
    children: dict = dataclasses.field(default_factory=dict)
    end: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def search_longest_prefix(self, word):
        node = self.root
        longest_prefix = ""
        current_prefix = ""
        for char in word:
            if char in node.children:
                current_prefix += char
                node = node.children[char]
                if node.end:
                    longest_prefix = current_prefix
            else:
                break
        return longest_prefix
