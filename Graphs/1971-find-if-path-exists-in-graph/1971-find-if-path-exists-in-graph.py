class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        visited = set()
        
        adj = [[] for _ in range(n)]
        
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        def dfs(here):
            if here in visited:
                return
            visited.add(here)
            
            for there in adj[here]:
                dfs(there)

        dfs(source)
        
        return True if destination in visited else False