'''
1. find the minimum price of prices
2. find the maximum price of prices after minimum price
3. return the profit by caculating maximum - mimimum
'''
# Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        모든 가능성을 하나하나 비교
        '''
        max_profit = 0
        for buy in range(0, len(prices)):
            for sell in range(buy+1, len(prices)):
                current_profit = prices[sell] - prices[buy]

                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit
'''
Time Complexity: O(n^2)
Space Complexity: O(1) two variables
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