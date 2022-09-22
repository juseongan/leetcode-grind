"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: Optional['Node']) -> List[List[int]]:
        if root is None:
            return []
        
        order = []
        queue = collections.deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
                level += [node.val]
            order.append(level)
        return order

# hyebin's solution
# way1. bfs
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        level_order = []
        queue = collections.deque([root] if root else [])

        while queue:
            level_order.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                level_order[-1].append(node.val)
                queue.extend(node.children)
        return level_order