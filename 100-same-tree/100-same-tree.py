# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(logN)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # p and q are both None
            return True
        
        if not q or not p or p.val != q.val: # one of p and q is None or have different val
            return False
        
        # recursively check the subtrees
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)