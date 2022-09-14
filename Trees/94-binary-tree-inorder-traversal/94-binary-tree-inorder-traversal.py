# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        self.helper(root, traversal)
        return traversal
    
    
    def helper(self, node, traversal):
        if node:
            self.helper(node.left, traversal)
            traversal.append(node.val)
            self.helper(node.right, traversal)