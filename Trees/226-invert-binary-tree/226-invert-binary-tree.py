# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        # recursively inverse the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root




# hyebin's solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])
        
        while queue:
            current_node = queue.popleft()
    
            
            if current_node:
                current_node.left, current_node.right = current_node.right, current_node.left
                
                queue.append(current_node.left)
                queue.append(current_node.right)
                
        return root
                
        