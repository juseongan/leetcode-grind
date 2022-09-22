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

# hyebin's solution
# way1. bfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []
        queue = collections.deque([root] if root else [])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_order.append(level)
        return level_order