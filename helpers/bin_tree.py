class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(tree_array: list[int]) -> TreeNode | None:
    # array = [root, root.left, root.right, root.left.left, 4, 5, 6] and root.val = array[0]
    if not tree_array:
        return None

    it = iter(tree_array)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root


#
# def create_array(root):
#     if not root:
#         return []
#
#     # Level traverse
#     l, q, node = [], [], root
#     while node:
#         l.append(node.val)
#         left, right = node.left, node.right
#         if left:
#             q.insert(0, left)
#         if right:
#             q.insert(0, right)
#         node = None if not q else q.pop()
#     return l
