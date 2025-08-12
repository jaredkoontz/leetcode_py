# https://leetcode.com/problems/insert-delete-getrandom-o1
import random

import pytest


class GetRandomVal:
    def __init__(self):
        self.data_map = {}  # dictionary, aka map, aka hashtable, aka hashmap
        self.data = []  # list aka array

    def insert(self, val: int) -> bool:
        # the problem indicates we need to return False if the item
        # is already in the RandomizedSet---checking if it's in the
        # dictionary is on average O(1) where as
        # checking the array is on average O(n)
        if val in self.data_map:
            return False

        # add the element to the dictionary. Setting the value as the
        # length of the list will accurately point to the index of the
        # new element. (len(some_list) is equal to the index of the last item +1)
        self.data_map[val] = len(self.data)

        # add to the list
        self.data.append(val)

        return True

    def remove(self, val: int) -> bool:
        # again, if the item is not in the data_map, return False.
        # we check the dictionary instead of the list due to lookup complexity
        if val not in self.data_map:
            return False

        # essentially, we're going to move the last element in the list
        # into the location of the element we want to remove.
        # this is a significantly more efficient operation than the obvious
        # solution of removing the item and shifting the values of every item
        # in the dictionary to match their new position in the list
        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]

        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list

        # change the last element in the list to now be the value of the element
        # we want to remove
        self.data[-1] = val

        # remove the last element in the list
        self.data.pop()

        # remove the element to be removed from the dictionary
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


RandomizedSet = GetRandomVal


@pytest.mark.parametrize(
    "operations, init, expected",
    [
        (
                [
                    "RandomizedSet",
                    "insert",
                    "remove",
                    "insert",
                    "getRandom",
                    "remove",
                    "insert",
                    "getRandom",
                ],
                [[], [1], [2], [2], [], [1], [2], []],
                [None, True, False, True, 2, True, False, 2],
        ),
    ],
)
def test_get_random(operations, init, expected):
    median_finder = None
    for op, components, curr_val in zip(operations, init, expected):
        if op == "RandomizedSet":
            median_finder = RandomizedSet()
        elif op == "insert":
            assert median_finder.insert(components[0]) == curr_val
        elif op == "remove":
            assert median_finder.remove(components[0]) == curr_val
        else:
            # 20 iterations seems like overkill, but sometimes we can get pretty unlucky.
            # But I can take 1 out of 1_048_576
            assert any(median_finder.getRandom() == curr_val for _ in range(20))
