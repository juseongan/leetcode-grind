# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Preorder Approach
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
        
# Postorder Approach
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def postorder(node):
            if node:
                return postorder(node.left) + postorder(node.right) + [node.val]
            else:
                return []
        
        return " ".join(map(str, postorder(root)))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        def postorder(lower = float('-inf'), upper = float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            
            val = data.pop()
            node = TreeNode(val)
            node.right = postorder(val, upper)
            node.left = postorder(lower, val)
            return node
        
        data = [int(x) for x in data.split(' ') if x]
        return postorder()