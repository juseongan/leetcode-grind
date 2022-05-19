# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        
        level = 0
        queue = collections.deque()
        if root: 
            queue.append(root)
            
        while queue:
            levels.append([]) # start the current level
            levLen = len(queue) # number of elements in the current level
            
            for i in range(levLen):
                node = queue.popleft()
                levels[level].append(node.val) # fulfill the current level
                
                if node.left: # add child nodes of the current level to the queue
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1 # next level
        
        return levels