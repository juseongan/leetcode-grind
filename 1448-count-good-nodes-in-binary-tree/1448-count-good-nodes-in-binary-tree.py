# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def goodNodes(self, root: TreeNode) -> int:
        num = 0
        
        def dfs(node, maxVal):
            nonlocal num
            if maxVal <= node.val:
                num += 1
            if node.right:
                dfs(node.right, max(node.val, maxVal))
            if node.left:
                dfs(node.left, max(node.val, maxVal))
        
        dfs(root, root.val)
        return num