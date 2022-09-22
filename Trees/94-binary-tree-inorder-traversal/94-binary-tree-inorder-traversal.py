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

# hyebin's solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_traversal = []
        
        def inorder(root, inorder_traversal):
            if root:
                inorder(root.left, inorder_traversal)
                inorder_traversal.append(root.val)
                inorder(root.right, inorder_traversal)
            
        inorder(root, inorder_traversal)
        return inorder_traversal
'''
n is the number of nodes
Time complexity: 2T(n/2) = O(n)
Space complexity: O(n)
'''