# hyebin's solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    longest_univalue_path = 0
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node):
            
            if node is None: return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val == node.val:
                left += 1
            else: 
                left = 0
                
            if node.right and node.right.val == node.val:
                right += 1
            else: 
                right = 0
                
            self.longest_univalue_path = max(self.longest_univalue_path, left+right)
            return max(left, right)
            
        dfs(root)
        return self.longest_univalue_path