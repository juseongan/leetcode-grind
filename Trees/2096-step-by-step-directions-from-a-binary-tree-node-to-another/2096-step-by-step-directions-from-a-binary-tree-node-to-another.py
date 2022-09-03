# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # LCA approach
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def getLCA(node: Optional[TreeNode]):
            # base cases
            if not node: return None
            if (node.val == startValue or node.val == destValue):
                return node
            left, right = getLCA(node.left), getLCA(node.right)
            if left and right:
                return node
            return left or right
        
        # find the LCA(Lowest Common Ancestor) of given two nodes
        lca = getLCA(root)
        # get the paths from LCA to the start, and LCA to the destination
        lcaToStart = lcaToDest = ""
        
        q = deque([(lca, '')])
        while q:
            node, path = q.popleft()
            if node.val == startValue:
                lcaToStart = path
                if lcaToDest: break
            if node.val == destValue:
                lcaToDest = path
                if lcaToStart: break
            if node.left: q.append((node.left, path+'L'))
            if node.right: q.append((node.right, path+'R'))
        
        # since we need to move up from start to LCA, convert all chars in lcaToStart to U
        return 'U'*len(lcaToStart) + lcaToDest