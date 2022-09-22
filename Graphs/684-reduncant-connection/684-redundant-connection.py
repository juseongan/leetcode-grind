# https://leetcode.com/problems/redundant-connection/
# hyebin's solution
# way1. recursive dfs
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(set)
        
        def dfs(here, destination):
            if here not in visited:
                visited.add(here) 
                if here == destination: return True
                return any(dfs(neighbor, destination) for neighbor in graph[here])
        
        for node1, node2 in edges:
            visited = set()
            if node1 in graph and node2 in graph and dfs(node1, node2):
                return node1, node2
            graph[node1].add(node2)
            graph[node2].add(node1)