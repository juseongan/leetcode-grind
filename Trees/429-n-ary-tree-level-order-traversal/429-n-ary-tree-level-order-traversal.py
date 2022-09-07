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