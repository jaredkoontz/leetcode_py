from collections import Counter

import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        return self.countPairs_rec(root, distance)

    @staticmethod
    def countPairs_rec(root: TreeNode, distance: int) -> int:
        count = 0

        def dfs(node):
            nonlocal count
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left_counts = dfs(node.left)
            right_counts = dfs(node.right)
            count += sum(
                left + right <= distance
                for left in left_counts
                for right in right_counts
            )
            return [n + 1 for n in left_counts + right_counts if n + 1 < distance]

        dfs(root)
        return count

    # todo finish
    @staticmethod
    def countPairs_stack(root: TreeNode, distance: int) -> int:
        stack = [(root, 0)]
        num_leaves = 0
        leaves = Counter()
        while stack:
            node, dist_from_root = stack.pop()
            if node.left:
                stack.append((node.left, dist_from_root + 1))
            if node.right:
                stack.append((node.right, dist_from_root + 1))
            if not (node.right and node.left):
                if leaves[dist_from_root]:
                    leaves[dist_from_root] += 1
                else:
                    leaves[dist_from_root] = 1
        for node, dist_from_root in leaves.items():
            wanted_distance = distance - dist_from_root
            if wanted_distance in leaves:
                min_leaves = min(leaves[dist_from_root], leaves[dist_from_root])
                num_leaves += min_leaves if min_leaves >= 0 else 0
                leaves[wanted_distance] -= 1
                leaves[node] -= 1

        return num_leaves


@pytest.mark.parametrize(
    "root,distance,expected",
    [
        ([1, 2, 3, None, 4], 3, 1),
        ([1, 2, 3, 4, 5, 6, 7], 3, 2),
        ([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2], 3, 1),
    ],
)
def test_num_good_leaf_pairs(root, distance, expected):
    assert Solution().countPairs(make_tree(root), distance) == expected
