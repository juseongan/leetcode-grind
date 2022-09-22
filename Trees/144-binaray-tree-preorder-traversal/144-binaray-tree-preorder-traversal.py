# hyebin's solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder_traversal = []
        
        def preorder(root, preorder_traversal):
            if root:
                preorder_traversal.append(root.val)
                preorder(root.left, preorder_traversal)
                preorder(root.right, preorder_traversal)
                
        preorder(root, preorder_traversal)
        return preorder_traversal