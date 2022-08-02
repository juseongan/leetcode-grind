class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        for i in range(2,len(cost)): # 2 <= cost.length
            cost[i] += min(cost[i-1],cost[i-2])
            
        return min(cost[-2],cost[-1])