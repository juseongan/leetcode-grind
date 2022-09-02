# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(depth)
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        values = []
        
        def dfs(node, depth):
            if not node:
                return
            
            if len(values) <= depth:
                values.append([])
            
            values[depth].append(node.val)
            
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            
        dfs(root, 0)
        
        return [sum(vals)/len(vals) for vals in values]