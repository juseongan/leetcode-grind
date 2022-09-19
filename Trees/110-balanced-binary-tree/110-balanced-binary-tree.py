# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        MAX = 10000
        
        def treeDepth(node):
            if not node:
                return 0
                
            LeftDepth = treeDepth(node.left)
            RightDepth = treeDepth(node.right)
            
            if abs(LeftDepth-RightDepth) > 1:
                return MAX
            
            return 1 + max(LeftDepth, RightDepth)
        
        if treeDepth(root) >= MAX:
            return False
        return True



# hyebin's solution (recursive way)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root is None: return -1
            
            left_height = check(root.left)
            right_height = check(root.right)
            
            if abs(left_height - right_height) > 1 or left_height == -2 or right_height == -2:
                return -2
            return max(left_height, right_height) + 1
        
        return check(root) != -2
'''
time complexity: 
space complexity: 
'''