class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        count = Counter(nums)
        
        return heapq.nlargest(k, count.keys(), key=count.get)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        numMap = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)
        for num, count in numMap.items():
            freq[count].append(num)
        
        topK = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                topK.append(n)
                if len(topK) == k:
                    return topK