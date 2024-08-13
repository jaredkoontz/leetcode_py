from collections import defaultdict
from collections import OrderedDict

import pytest


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insertHead(self, node):
        head_nxt = self.head.next
        head_nxt.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = head_nxt
        self.size += 1

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def removeTail(self):
        last = self.tail.prev
        self.removeNode(last)
        return last


class DLinkedList:
    def __init__(self):
        self.sentinel = Node(0, 0)
        self.sentinel.next = self.sentinel.prev = self.sentinel
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, node):
        node.next = self.sentinel.next
        node.prev = self.sentinel
        node.next.prev = node
        self.sentinel.next = node
        self.size += 1

    def pop(self, node=None):
        if self.size == 0:
            return
        if not node:
            node = self.sentinel.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node


class LFUCacheOrderedDict:
    def __init__(self, capacity: int):
        self.cache = {}
        self.frequencies = defaultdict(OrderedDict)
        self.min_freq = 0
        self.capacity = capacity

    def _insert(self, key: int, frequency: int, value: int):
        self.cache[key] = (frequency, value)
        self.frequencies[frequency][key] = value

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        frequency, value = self.cache[key]
        del self.frequencies[frequency][key]
        if not self.frequencies[frequency]:
            del self.frequencies[frequency]
            if frequency == self.min_freq:
                self.min_freq += 1
        self._insert(key, frequency + 1, value)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.cache:
            frequency = self.cache[key][0]
            self.cache[key] = (frequency, value)
            self.get(key)
            return
        if self.capacity == len(self.cache):
            key_to_delete, frequency = self.frequencies[self.min_freq].popitem(
                last=False
            )
            del self.cache[key_to_delete]
        self.min_freq = 1
        self._insert(key, 1, value)


class LFUCacheDLL:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.freq = defaultdict(DLinkedList)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        freq = node.freq
        self.freq[freq].pop(node)
        if len(self.freq[freq]) == 0:
            del self.freq[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        node.freq += 1
        self.freq[node.freq].append(node)
        self.cache[key] = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return
        if self.cap == len(self.cache):
            deleted = self.freq[self.min_freq].pop()
            del self.cache[deleted.key]
        node = Node(key, value)
        self.cache[key] = node
        self.freq[1].append(node)
        self.min_freq = 1


class LFUCacheDLL2:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.freq = defaultdict(DLL)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        freq = node.freq
        self.freq[freq].removeNode(node)
        if self.freq[freq].size == 0:
            del self.freq[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        node.freq += 1
        self.freq[node.freq].insertHead(node)
        self.cache[key] = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return
        if self.cap == len(self.cache):
            deleted = self.freq[self.min_freq].removeTail()
            del self.cache[deleted.key]
        node = Node(key, value)
        self.cache[key] = node
        self.freq[1].insertHead(node)
        self.min_freq = 1


LFUCache = LFUCacheOrderedDict


@pytest.mark.parametrize(
    "operations, init, expected",
    [
        (
            [
                "LFUCache",
                "put",
                "put",
                "get",
                "put",
                "get",
                "get",
                "put",
                "get",
                "get",
                "get",
            ],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, 3, None, -1, 3, 4],
        ),
    ],
)
def test_lfu_cache(operations, init, expected):
    cache = None
    for op, components, curr_val in zip(operations, init, expected):
        if op == "LFUCache":
            cache = LFUCache(components[0])
        elif op == "put":
            cache.put(components[0], components[1])
        else:
            assert cache.get(components[0]) == curr_val
