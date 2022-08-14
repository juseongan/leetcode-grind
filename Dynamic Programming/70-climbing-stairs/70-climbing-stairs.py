'''
There are 3 ways to get to the top
a. 1step + 1step + 1step
b. 1step + 2step
c. 2step + 1step
'''

# Bruth Force -> Time Limit Exceeded!
'''
Like fibonacci
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
'''
Time Complexity: O(n)
Space Complexity: O(n)
'''



# Dynamic Programming (Memorization)     
class Solution:
    dp = collections.defaultdict(int) # dp: Keeping track of how many different ways

    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        if dp[n]:
            return dp[n]

        dp[n] = climbStairs(n-1) +  climbStairs(n-2) # check if you have already solve clibStairs(n-1) or clibStairs(n-2)
        return dp[n]
'''
Time complexity: O(n)
Space complexity: O(n)
'''



# Dynamic Programming (Tablation)  
class Solution:
    dp = collections.defaultdict(int) # dp: Keeping track of how many different ways

    def climbStairs(self, n: int) -> int:
        dp[1] = 1
        dp[2] = 2 # 1step + 1step or 2step

        for ways in range(3, (n+1)):
            dp[ways] = dp[ways-1] + dp[ways-2]

        return dp[n]
'''
Time complexity: O(n)
Space complexity: O(n): dp array of size n is used.
'''