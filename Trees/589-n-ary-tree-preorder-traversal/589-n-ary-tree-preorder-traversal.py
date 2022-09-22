# hyebin's solution
# way1. recursive 
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        n_ary_preorder = []
        self.nary(root, n_ary_preorder)
        return n_ary_preorder
        
    def nary(self, root, n_ary_preorder):
        if root:
            n_ary_preorder.append(root.val)
            for child in root.children:
                self.nary(child, n_ary_preorder)

# hyebin's solution
# way2. literative
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None: return []
        stack = [root]
        n_ary_tree = []
        
        while stack:
            temp = stack.pop()
            n_ary_tree.append(temp.val)
            stack.extend(temp.children[::-1])
        return n_ary_tree