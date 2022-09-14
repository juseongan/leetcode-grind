# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(logN)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0 
        
        else: 
            leftHeight = self.maxDepth(root.left) 
            rightHeight = self.maxDepth(root.right) 
            
            return max(leftHeight, rightHeight) + 1 




# hyebin's solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None: return 0
        
        queue = collections.deque([root])
        depth = 0
        
        while queue:
            depth += 1
            
            for _ in range(len(queue)):
                current_node = queue.popleft()
                
                if current_node.left: 
                    queue.append(current_node.left)
                if current_node.right: 
                    queue.append(current_node.right)
            
        return depth