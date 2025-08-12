# https://leetcode.com/problems/most-frequent-subtree-sum
import collections

import pytest

from helpers.bin_tree import TreeNode
from helpers.bin_tree import make_tree


class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        return self.findFrequentTreeSum_dfs_stack(root)

    @staticmethod
    def findFrequentTreeSum_dfs_stack(root: TreeNode | None) -> list[int]:
        if not root:
            return []

        # Map to count the frequency of each subtree sum
        freq_map = collections.defaultdict(int)
        stack = collections.deque()
        visited = set()
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack[-1]

            # Check if we have visited the right child
            if curr.right and curr.right not in visited:
                curr = curr.right
            else:
                stack.pop()
                visited.add(curr)

                # Calculate the subtree sum
                left_sum = curr.left.val if curr.left else 0
                right_sum = curr.right.val if curr.right else 0
                curr_sum = left_sum + right_sum + curr.val

                # Store the sum in the node itself to avoid a separate map
                curr.val = curr_sum

                freq_map[curr_sum] += 1

                curr = None

        max_count = max(freq_map.values())
        result = [s for s in freq_map if freq_map[s] == max_count]

        return result

    @staticmethod
    def findFrequentTreeSum_dfs(root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        count = collections.Counter()

        def dfs(node):
            if node is None:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            count[s] += 1
            return s

        dfs(root)
        max_count = max(count.values())
        return [s for s in count if count[s] == max_count]


@pytest.mark.parametrize(
    "root,expected",
    [
        ([5, 2, -3], [2, -3, 4]),
        ([5, 2, -5], [2]),
    ],
)
def test_findFrequentTreeSum(root, expected):
    assert Solution().findFrequentTreeSum(make_tree(root)) == expected
