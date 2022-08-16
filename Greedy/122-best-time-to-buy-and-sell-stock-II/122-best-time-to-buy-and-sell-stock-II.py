'''
Sell before the stock price falls and buy before it rises.
'''
# Greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Declare variable
        gain = 0
        
        # Accumulate profit
        for price in range(0, len(prices)):
            
            if prices[price+1] > prices[price]:
                gain += prices[price+1] - prices[price]
                
        return gain
            
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''

# Pythonic way
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 매번 이익일 때마다 합산
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''