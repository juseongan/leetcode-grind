class Solution:
    # Time Complexity: O(NlogN)
    # Space Complexity: O(n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        
        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        
        kPoints = []
        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            kPoints.append([x, y])
        
        return kPoints