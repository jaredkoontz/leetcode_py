# https://leetcode.com/problems/path-sum-ii
from collections import deque

import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        assert (
            self.pathSum_mine(root, targetSum)
            == self.pathSum_recursive(root, targetSum)
            == self.pathSum_dfs(root, targetSum)
            == self.pathSum_dfs_stack(root, targetSum)
            == self.pathSum_dfs_stack_ii(root, targetSum)
            == self.pathSum_bfs_queue(root, targetSum)
        )
        return self.pathSum_mine(root, targetSum)

    @staticmethod
    def pathSum_mine(root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root:
            return []

        all_paths = []
        queue = deque([(root, 0, [root.val])])
        while len(queue):
            root, current_sum, current_path = queue.pop()
            current_sum = current_sum + root.val
            if not root.left and not root.right:
                if current_sum == targetSum:
                    all_paths.append(current_path)
            if root.right:
                queue.append((root.right, current_sum, current_path + [root.right.val]))
            if root.left:
                queue.append((root.left, current_sum, current_path + [root.left.val]))
        return all_paths

    def pathSum_recursive(
        self, root: TreeNode | None, targetSum: int
    ) -> list[list[int]]:
        if not root:
            return []
        if not root.left and not root.right and targetSum == root.val:
            return [[root.val]]
        tmp = self.pathSum_recursive(
            root.left, targetSum - root.val
        ) + self.pathSum_recursive(root.right, targetSum - root.val)
        return [[root.val] + i for i in tmp]

    @staticmethod
    def pathSum_dfs(root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []

        def dfs(node, total_sum, curr_list, curr_result):
            if node:
                if not node.left and not node.right and total_sum == node.val:
                    curr_list.append(node.val)
                    curr_result.append(curr_list)
                dfs(
                    node.left, total_sum - node.val, curr_list + [node.val], curr_result
                )
                dfs(
                    node.right,
                    total_sum - node.val,
                    curr_list + [node.val],
                    curr_result,
                )

        dfs(root, targetSum, [], result)
        return result

    @staticmethod
    def pathSum_dfs_stack(root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root:
            return []
        res = []
        stack = [(root, targetSum - root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val - curr.right.val, ls + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, val - curr.left.val, ls + [curr.left.val]))
        return res

    @staticmethod
    def pathSum_dfs_stack_ii(root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == targetSum:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls + [curr.left.val]))
        return res

    @staticmethod
    def pathSum_bfs_queue(root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == targetSum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val + curr.left.val, ls + [curr.left.val]))
            if curr.right:
                queue.append((curr.right, val + curr.right.val, ls + [curr.right.val]))
        return res


@pytest.mark.parametrize(
    "l1,leaf_sum,expected",
    [
        (
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 5, 1],
            22,
            [[5, 4, 11, 2], [5, 8, 4, 5]],
        ),
        ([1, 2, 3], 5, []),
        ([4, 9, 0, 5, 1], 14, [[4, 9, 1]]),
        ([1, 2, 3], 4, [[1, 3]]),
        ([1, 5, 2, 3, 4], 3, [[1, 2]]),
        ([], 0, []),
        ([1], 1, [[1]]),
    ],
)
def test_sumNumbers(l1, leaf_sum, expected):
    assert Solution().pathSum(make_tree(l1), leaf_sum) == expected
