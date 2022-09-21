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