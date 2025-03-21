import dataclasses
from collections import deque


@dataclasses.dataclass
class NAryNode:
    val: int = 0
    children: list["NAryNode"] = dataclasses.field(default_factory=list)


def make_nary_tree(data: list[list[int | None]]) -> NAryNode | None:
    if not data:
        return None

    root = NAryNode(data[0])
    queue = deque([root])
    # index is 2 because we grab the root and skip the first null
    index = 2

    while queue and index < len(data):
        current = queue.popleft()
        children = []

        # Collect all children until the next None separator
        while index < len(data) and data[index] is not None:
            child = NAryNode(data[index])
            children.append(child)
            queue.append(child)
            index += 1

        # Assign collected children to the current node
        current.children = children
        # Skip the None separator for the current node's children
        index += 1

    return root
