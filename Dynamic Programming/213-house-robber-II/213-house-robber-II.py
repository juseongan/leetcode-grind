class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
            
        if N <= 3:
            return max(nums)
        
        max_money = 0
        for remove_idx in range(N):
            temp = nums
            temp = temp[remove_idx:] + temp[:remove_idx]
            
            dp = temp
            
            for i in range(2,N-1):
                dp[i] += max(temp[:i-1])
            
            max_money = max(max_money, max(dp))
        
        return max_money