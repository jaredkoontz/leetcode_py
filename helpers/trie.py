import dataclasses


@dataclasses.dataclass
class TrieNode:
    letter: str
    is_end: bool = False
    children: dict[str, "TrieNode"] = dataclasses.field(default_factory=dict)


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = TrieNode(char)
                node = node.children[char]
        else:
            node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        else:
            return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        else:
            return True

    def search_longest_prefix(self, word: str):
        node = self.root
        longest_prefix = ""
        current_prefix = ""
        for char in word:
            if char in node.children:
                current_prefix += char
                node = node.children[char]
                if node.is_end:
                    longest_prefix = current_prefix
            else:
                break
        return longest_prefix
