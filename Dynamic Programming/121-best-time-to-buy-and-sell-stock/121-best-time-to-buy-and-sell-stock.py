# hyebin's solution
'''
Algorithm
1. Find the minimum price of prices[i]
2. Find the maximum price of prices[i] after prices[minimum] position
3. Return the profit by caculating maximum - mimimum
'''

class Solution:
    '''
    Write processing
    Input: prices = [7,1,5,3,6,4]
    
    find_minimum(100001): 100001, 7 -> 7 # 굳이 필요하지 않아보임
    👇 부터 진행하면 될 것 같음
    find_minimum'7': compare 7 and 1 -> 1
        maximum_profit'0': compare 0 and 0-1 -> 0
    find_minimum'1': compare 1 and 5 -> 1
        maximum_profit'0': compare 0 and 5-1 -> 4
    find_minimum'1': compare 1 and 3 -> 1
        maximum_profit'4': compare 4 and 3-1 -> 4
    find_minimum'1': compare 1 and 6 -> 1
        maximum_profit'4': compare 4 and 6-1 -> 5
    find_minimum'1': compare 1 and 4 -> 1
        maximum_profit'5': compare 5 and 4-1 -> 5
        
    Output: the maximum profit'5'
    '''
    # input: prices[i] is the price of a given stock on the i day
    def maxProfit(self, prices: List[int]) -> int:
        
        # Declare varibale
        find_minimum = prices[0]
        maximum_profit = 0
        
        # Find the maximum profit
        for index in range(1, len(prices)): # index 1 to len(prices)-1
            find_minimum = min(find_minimum, prices[index])
            maximum_profit = max(maximum_profit, prices[index] - find_minimum)
            
        return maximum_profit
'''
Time complexity: O(n) for loop  
Space complexity: O(1) using 2 variable find_minimum, maximum_profit
'''