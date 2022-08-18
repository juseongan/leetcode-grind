# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # data type of output is list
        inorder_traversal = []
        
        def inorder(node, inorder_traversal):
            
            if node is None:
                return
            
            inorder(node.left, inorder_traversal)
            inorder_traversal.append(node.val)
            inorder(node.right, inorder_traversal)
            
        inorder(root, inorder_traversal)
        return inorder_traversal
'''
n is the number of nodes
Time complexity: 2T(n/2) = O(n)
Space complexity: O(n)
'''