# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        
        while node: # traverse the tree
            if p.val < node.val and q.val < node.val: # go onto the left subtree
                node = node.left
            elif p.val > node.val and q.val > node.val: # go onto the right subtree
                node = node.right
            else: # found the split point return the LCA node
                return node