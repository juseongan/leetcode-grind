class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        left = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right

            maxProfit = max(maxProfit, prices[right] - prices[left])
                
        return maxProfit