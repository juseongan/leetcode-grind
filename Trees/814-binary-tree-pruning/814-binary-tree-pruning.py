# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def containsOne(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            
            # check if any node in the subtrees contains a 1
            leftSubtree = containsOne(node.left)
            rightSubtree = containsOne(node.right)
            
            # remove subtrees without a 1
            if not leftSubtree:
                node.left = None
            if not rightSubtree:
                node.right = None
            
            # return true if the current node or its left/right subtrees contains a 1
            return node.val or leftSubtree or rightSubtree
        
        return root if containsOne(root) else None