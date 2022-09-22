class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaves = []
        
        def dfs(node):
            if not node:
                return -1
            
            height = max(dfs(node.left), dfs(node.right)) + 1
            if height >= len(leaves):
                leaves.append([])
            
            leaves[height].append(node.val)
            return height
        
        dfs(root)
        
        return leaves