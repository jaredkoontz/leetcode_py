# https://leetcode.com/problems/path-sum-iii
from collections import deque

import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        return self.pathSum_recursive(root, targetSum)

    @staticmethod
    def pathSum_queue(root: TreeNode | None, targetSum: int) -> int:
        if root is None:
            return 0
        queue = [(root, [])]
        res = 0
        while queue:
            node, ans = queue.pop(0)
            curr_ans = []
            if node.val == targetSum:
                res += 1
            for val in ans:
                sum_val = val + node.val
                if sum_val == targetSum:
                    res += 1
                curr_ans.append(sum_val)
            curr_ans.append(node.val)
            if node.left:
                queue.append((node.left, curr_ans))
            if node.right:
                queue.append((node.right, curr_ans))
        return res

    # todo fails
    @staticmethod
    def pathSum_mine(root: TreeNode | None, targetSum: int) -> int:
        if root is None:
            return 0

        queue = deque([(root, root.val, {})])
        all_sums = 0

        while queue:
            node, path_sum, local_cache = queue.popleft()
            node_val = node.val
            # path_sum += node_val
            # node itself equals
            if node_val == targetSum:
                all_sums += 1

            old_path_sum = path_sum - targetSum
            # update result and cache
            all_sums += local_cache.get(old_path_sum, 0)
            # todo updates cache for all nodes in queue
            local_cache[path_sum] = local_cache.get(path_sum, 0) + 1

            if node.left:
                queue.append((node.left, node.left.val, local_cache))
            if node.right:
                queue.append((node.right, node.right.val, local_cache))
            # local_cache[path_sum] -= 1

        return all_sums

    RECURSIVE_RESULT = 0

    def pathSum_recursive(self, root, target):
        # define global result and path
        cache = {0: 1}

        def dfs(node, current_target, curr_path_sum, my_cache):
            # exit condition
            if node is None:
                return
                # calculate currPathSum and required old_path_sum
            curr_path_sum += node.val
            old_path_sum = curr_path_sum - current_target
            # update result and cache
            self.RECURSIVE_RESULT += my_cache.get(old_path_sum, 0)
            my_cache[curr_path_sum] = my_cache.get(curr_path_sum, 0) + 1

            # dfs breakdown
            dfs(node.left, current_target, curr_path_sum, my_cache)
            dfs(node.right, current_target, curr_path_sum, my_cache)
            # when move to a different branch, the currPathSum is no longer available, hence remove one.
            my_cache[curr_path_sum] -= 1

        # recursive to get result
        dfs(root, target, 0, cache)

        # return result
        return self.RECURSIVE_RESULT


@pytest.mark.parametrize(
    "l1,target_sum,expected",
    [
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3),
    ],
)
def test_path_sum_3(l1, target_sum, expected):
    assert Solution().pathSum(make_tree(l1), target_sum) == expected
