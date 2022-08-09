'''

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Declare variable
        gain = 0
        
        # Accumulate profit
        for i in range(len(prices)-1):
            
            if prices[i+1] > prices[i]:
                gain += prices[i+1] - prices[i]
                
        return gain
            
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''