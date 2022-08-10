class Solution:
    # Time Complexity: O(NlogN)
    # Space Complexity: O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): # makes the stones negative so we have a max heap
            stones[i] *= -1
            
        heapq.heapify(stones)
        
        while len(stones) > 1:
            firstS = heapq.heappop(stones)
            secondS = heapq.heappop(stones)
            
            if firstS != secondS:
                heapq.heappush(stones, firstS - secondS)
        
        # convert the stone back to positive
        return -heapq.heappop(stones) if stones else 0