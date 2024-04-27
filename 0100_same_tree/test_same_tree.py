import pytest

from helpers.bin_tree import make_tree
from helpers.bin_tree import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        assert (
            self.isSameTree_dfs(p, q)
            == self.isSameTree_bfs(p, q)
            == self.isSameTree_clean(p, q)
            == self.isSameTree_mine(p, q)
        )
        return self.isSameTree_clean(p, q)

    @staticmethod
    def isSameTree_dfs(p: TreeNode | None, q: TreeNode | None) -> bool:
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if n1 and n2 and n1.val == n2.val:
                stack.append((n1.right, n2.right))
                stack.append((n1.left, n2.left))
            elif n1 != n2:
                return False
        return True

    @staticmethod
    def isSameTree_bfs(p: TreeNode | None, q: TreeNode | None) -> bool:
        queue = [(p, q)]
        while queue:
            node1, node2 = queue.pop(0)
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
        return True

    def isSameTree_clean(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p and q:
            return (
                p.val == q.val
                and self.isSameTree_clean(p.left, q.left)
                and self.isSameTree_clean(p.right, q.right)
            )
        return p is q

    def isSameTree_mine(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            if p.val == q.val:
                return self.isSameTree_mine(p.left, q.left) and self.isSameTree_mine(
                    p.right, q.right
                )
            else:
                return False


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
    ],
)
def test_isSameTree(l1, l2, expected):
    assert Solution().isSameTree(make_tree(l1), make_tree(l2)) == expected
