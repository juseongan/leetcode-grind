# hyochan's solution
# dijkstra
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = {}
        nodes = set()
        
        # Initialize adjacency list
        for equation in equations:
            node1, node2 = equation
            if node1 not in adj: adj[node1] = []
            if node2 not in adj: adj[node2] = []
        
        # Save the graph in the adjacency list
        for equation, value in zip(equations, values):
            node1, node2 = equation
            nodes.add(node1)
            nodes.add(node2)
            adj[node1].append([value, node2])
            adj[node2].append([1/value, node1])
        
        # Dijkstra's to find the shortest distance between 2 nodes
        def dijkstras(start_node, end_node):
            priority_queue = [(0, start_node)]
            heapq.heapify(priority_queue)
            distance = {start_node:1.0}
            visited = set([start_node])
            
            while priority_queue:
                dist_here, here = heapq.heappop(priority_queue)
                
                for edge, there in adj[here]:
                    if there in visited: continue
                    visited.add(there)
                    
                    if there not in distance:
                        distance[there] = distance[here] * edge 
                    else:    
                        if distance[there] > distance[here] * edge:
                            distance[there] = distance[here] * edge
                    
                    priority_queue.append((distance[there], there))
            
            return -1 if end_node not in distance else distance[end_node]
                
        answer = []
        for query in queries:
            val = None
            node1, node2 = query
            if node1 not in nodes or node2 not in nodes:
                val = -1.0
            elif node1 == node2:
                val = 1.0
            else:
                val = dijkstras(node1, node2)
            answer.append(val)
        
        return answer