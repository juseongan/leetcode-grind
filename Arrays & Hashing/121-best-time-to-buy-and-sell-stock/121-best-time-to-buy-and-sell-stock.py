'''
1. We need to find the minimum price of prices[i]
2. We need to find the maximum price of prices[i] after prices[minimum] position
3. We need to return the profit by caculating maximum - mimimum
'''


class Solution:
    # input: prices[i] is the price of a given stock on the i day
    def maxProfit(self, prices: List[int]) -> int:
        
        # Declare varibale
        min_price = sys.maxsize 
        profit = 0
        
        # Find the maximum profit
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
            
        return profit
    
'''
Time Complexity: O(n) 
Space Complexity: O(1) 
'''