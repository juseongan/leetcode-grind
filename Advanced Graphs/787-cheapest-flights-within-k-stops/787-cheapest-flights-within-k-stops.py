class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # We use two arrays for storing distances and keep swapping
        # between them to save on the memory
        distances = [[float('inf')] * n for _ in range(2)]
        distances[0][src] = distances[1][src] = 0
        
        # K + 1 iterations of Bellman Ford
        for iterations in range(K + 1):
            
            # Iterate over all the edges
            for s, d, wUV in flights:
                
                # Current distance of node "s" from src
                dU = distances[1 - iterations&1][s]
                
                # Current distance of node "d" from src
                # Note that this will port existing values as
                # well from the "previous" array if they didn't already exist
                dV = distances[iterations&1][d]
                
                # Relax the edge if possible
                if dU + wUV < dV:
                    distances[iterations&1][d] = dU + wUV
                    
        return -1 if distances[K&1][dst] == float("inf") else distances[K&1][dst]