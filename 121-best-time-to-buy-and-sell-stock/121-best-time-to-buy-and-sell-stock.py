class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        
        for buyDay in range(1, len(prices)):
            if prices[buyDay] < minPrice:
                minPrice = prices[buyDay]
            elif prices[buyDay] - minPrice > maxProfit:
                maxProfit = prices[buyDay] - minPrice
                
        return maxProfit