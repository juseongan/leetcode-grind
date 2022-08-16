class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        
        if N <= 2:
            return max(nums)
        
        dp = nums
        
        # bottom up approach with dynamic programming
        for i in range(2, N):
            dp[i] = dp[i] + max(nums[:i-1])
        
        return max(dp)


        
'''
If I choose to rob current house, I will have to skip the next house on the house street.

main problem | sub problem
rob          = max(rob_house[0]+rob_house[2:last house], rob_house[1:last house])
'''
# Recursive Brute Force -> Time Limit Exceeded!
class Solution: 
    def rob(self, nums: List[int]) -> int: # nums: representing not index but the amount of money of each house
        
        def rob_house(current_house: int) -> int:
            # Base case
            if current_house < 0:
                return 0

            return max(rob_house(current_house-1), rob_house(current_house-2)+nums[current_house])
            '''
            More explaination
            house street | 8 | 7 | 3 | 9 |
            rob house    | 8 | 8 |11 | 17|

            house street | 9 | 3 | 9 | 8 |
            rob house    | 9 | 9 |18 | 18|
            '''
    
        return rob_house(len(nums)-1)
'''
Time Complexity: O(n)
Space Complexity: O(n): Two 1D array
'''



# Dynamic Programming (Tablation)  
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Base case
        if len(nums) <=2:
            return max(nums)
        
        dp = collections.defaultdict(int) # dp는 테이블 형식으로 데이터를 저장하니깐 dict 사용!
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for current_house in range(2, len(nums)):
            dp[current_house] = max(dp[current_house-1], dp[current_house-2]+nums[current_house]) 
        
        return dp[len(nums)-1]
'''
Time Complexity: O(n)
Space Complexity: O(n): Two 1D array
'''