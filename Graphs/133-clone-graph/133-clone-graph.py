# Iterative BFS Approach
class Solution:
    # Time Complexity: O(V + E)
    # Space Complexity: O(V)
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        queue = deque([node])
        clones = {node.val: Node(node.val)}
        
        while queue:
            curNode = queue.popleft()
            curClone = clones[curNode.val]
            
            for neighbor in curNode.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                
                curClone.neighbors.append(clones[neighbor.val])       
        
        return clones[node.val]

# Iterative DFS Approach
class Solution:
    # Time Complexity: O(V + E)
    # Space Complexity: O(V)
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        stack = [node]
        clones = {node.val: Node(node.val)}
        
        while stack:
            curNode = stack.pop()
            curClone = clones[curNode.val]
            
            for neighbor in curNode.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val)
                    stack.append(neighbor)
                
                curClone.neighbors.append(clones[neighbor.val])       
        
        return clones[node.val]

# Recursive DFS Approach
class Solution:
    # Time Complexity: O(V + E)
    # Space Complexity: O(V)
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        clones = {}
        def dfs(curNode):
            if curNode in clones:
                return clones[curNode]

            curClone = Node(curNode.val)
            clones[curNode] = curClone
            for nei in curNode.neighbors:
                curClone.neighbors.append(dfs(nei))
            return curClone

        return dfs(node)