'''
1. find the minimum price of prices
2. find the maximum price of prices after minimum price
3. return the profit by caculating maximum - mimimum
'''

# Dynamic Programming 
class Solution:
    # input: prices[i] is the price of a given stock on the i day
    def maxProfit(self, prices: List[int]) -> int:
        
        # Declare varibale
        min_price = sys.maxsize 
        max_profit = 0
        
        # Find the maximum profit
        for price in prices:
            min_price = min(min_price, price)
            '''
            if prices[price] < min_price:
                min_price = prices[price] 
            '''
            max_profit = max(max_profit, price - min_price)
            '''
            elif prices[price] - min_price > max_profit:
                max_profit = prices[price] - min_price
            '''
        return max_profit  
'''
Time Complexity: O(n) 
Space Complexity: O(1) 
'''