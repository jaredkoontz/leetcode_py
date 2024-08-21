# https://leetcode.com/problems/lru-cache
from collections import OrderedDict

import pytest


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCacheOrderedDict:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key: int):
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key: int, val: int):
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)


class LRUCacheShorter:
    def __init__(self, MSize):
        self.size = MSize
        self.cache = {}
        self.next, self.before = {}, {}
        self.head, self.tail = "#", "$"
        self.connect(self.head, self.tail)

    def connect(self, a, b):
        self.next[a], self.before[b] = b, a

    def delete(self, key):
        self.connect(self.before[key], self.next[key])
        del self.before[key], self.next[key], self.cache[key]

    def append(self, k, v):
        self.cache[k] = v
        self.connect(self.before[self.tail], k)
        self.connect(k, self.tail)
        if len(self.cache) > self.size:
            self.delete(self.next[self.head])

    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.delete(key)
        self.append(key, val)
        return val

    def put(self, key, value):
        if key in self.cache:
            self.delete(key)
        self.append(key, value)


class LRUCacheMine:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # left is LRU, right is most recently
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    @staticmethod
    def _remove(node: Node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node: Node):
        """inserts at the right"""
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            n = self.cache[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        n = Node(key, value)
        self._add(n)
        self.cache[key] = n
        if len(self.cache) > self.capacity:
            # remove from the list and delete the LRU from the hash map
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]


LRUCache = LRUCacheOrderedDict


@pytest.mark.parametrize(
    "operations, init, expected",
    [
        (
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, None, -1, 3, 4],
        ),
    ],
)
def test_lru_cache(operations, init, expected):
    cache = None
    for op, components, curr_val in zip(operations, init, expected):
        if op == "LRUCache":
            cache = LRUCache(components[0])
        elif op == "put":
            cache.put(components[0], components[1])
        else:
            assert cache.get(components[0]) == curr_val
