# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        sequence = ""
        def traversal(node):    # pre-order traversal
            nonlocal sequence   # ~global, can modify surrounding function's scope.

            if node is None:
                sequence += "null,"
            else:
                sequence += str(node.val) + ","
                traversal(node.left)
                traversal(node.right)

        traversal(root)
        
        return sequence

    def deserialize(self, data: str) -> Optional[TreeNode]:
        dataList = data.split(",")
        
        def traversal(dataList):    # pre-order traversal
            if dataList[0] == "null":
                dataList.pop(0)
                return None
            
            node = TreeNode(dataList[0])
            dataList.pop(0)
            
            node.left = traversal(dataList)
            node.right = traversal(dataList)
            
            return node
        
        root = traversal(dataList)
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans