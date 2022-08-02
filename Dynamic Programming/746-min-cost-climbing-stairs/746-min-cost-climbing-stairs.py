class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        for i in range(2,len(cost)): # 2 <= cost.length
            cost[i] += min(cost[i-1],cost[i-2])
            
        return min(cost[-2],cost[-1])

# Fibonacci Number Solution
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second