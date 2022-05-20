# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, lower, upper): # helper function to validate if node is within lower and upper limit
            if not node: # empty trees are valid
                return True
            
            if node.val <= lower or node.val >= upper:
                return False
            
            return (validate(node.left, lower, node.val) and # validate the left and right subtrees
                    validate(node.right, node.val, upper))
        
        return validate(root, -math.inf, math.inf)