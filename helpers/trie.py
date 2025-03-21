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


def _collect_from_node(node: TrieNode, prefix: str, limit=-1):
    words = []
    stack = [(node, prefix)]
    while stack:
        node, prefix = stack.pop()
        children = node.children
        if not children or node.end:
            words.append(prefix)
        for idx, curr in node.children.items():
            stack.append((curr, f'{prefix}{chr(idx + ord("0"))}'))

    if limit >= 0:
        return sorted(words)[:limit]
    else:
        return words


def traverse_trie_from_term(node: TrieNode, search_term: str):
    cur = node
    count = 0
    curr_prefix = ""
    for ch in str(search_term):
        idx = ord(ch) - ord("0")
        curr_prefix += ch
        if cur.children.get(idx) is None:
            return []
        cur = cur.children[idx]
        count += 1
    return _collect_from_node(cur, curr_prefix, limit=3)


def prefix_count(node: TrieNode, new_word: str):
    cur = node
    count = 0
    for ch in str(new_word):
        idx = ord(ch) - ord("0")
        if cur.children.get(idx) is None:
            return count
        cur = cur.children[idx]
        count += 1
    return count


def add_to_trie(node: TrieNode, new_word: str):
    cur = node
    for ch in new_word:
        idx = ord(ch) - ord("0")
        if cur.children.get(idx) is None:
            cur.children[idx] = TrieNode()
        cur = cur.children[idx]
    cur.end = True
