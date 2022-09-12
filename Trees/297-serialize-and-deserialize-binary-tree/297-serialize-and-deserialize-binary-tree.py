# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        result = ['X']
        
        while queue:
            node = queue.popleft()
            
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
                
            else:
                result.append('X')
                
        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'X X':
            return None
        
        nodes = data.split()
        
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        
        while queue:
            node = queue.popleft()
            
            if nodes[index] is not 'X':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)     
            index += 1
            
            if nodes[index] is not 'X':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
            
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))