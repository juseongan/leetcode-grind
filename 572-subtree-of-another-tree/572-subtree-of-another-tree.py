# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # Time Complexity: O(S*T)
    # Space Complexity: O(logN)
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        else: # recursively check the subtrees
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    # Time Complexity: O(n)
    # Space Complexity: O(logN)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # p and q are both None
            return True
        
        if not q or not p or p.val != q.val: # one of p and q is None or have different val
            return False
        
        # recursively check the subtrees
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)