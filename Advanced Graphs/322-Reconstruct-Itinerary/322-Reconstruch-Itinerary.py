class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for departure, arrival in sorted(tickets):
            graph[departure ].append(arrival)
        
        route = [] # storing the order
        def dfs(departure):
            while graph[departure]:
                dfs(graph[departure].pop(0))
            route.append(departure)
            
        dfs("JFK") # calling dfs 
        
        return route[::-1]