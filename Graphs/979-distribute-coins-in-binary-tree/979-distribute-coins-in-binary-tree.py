# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root):
        '''
        if root is [3,0,0]
        
        TreeNode{
            val: 3, 
            left: TreeNode{val: 0, left: None, right: None},
            right: TreeNode{val: 0, left:None, right: None}
        
        }
        '''
        self.move = 0
        
        def dfs(node):

            if node is None: return 0
            
            leftstep = dfs(node.left)
            rightstep = dfs(node.right)
            self.move += abs(leftstep) + abs(rightstep)
            return node.val + leftstep + rightstep -1
            
        dfs(root)
        return self.move

            