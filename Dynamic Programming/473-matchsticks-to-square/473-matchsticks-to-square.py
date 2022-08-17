# back tracking -> Time Limit Exceeded!
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        square_length = sum(matchsticks)  // 4
        sides = [0] * 4
        
        if sum(matchsticks) / 4 != square_length:
            return False
        
        # if length = 2, matchsticks[0] = 3, it can not make squre.
        matchsticks.sort(reverse=True)
        
        def backtrack(i):
            # base case
            # 'i' is index
            if i == len(matchsticks): return True
            
            # fill up w e n s
            for side in range(4):
                if sides[side] + matchsticks[i] <= square_length:
                    sides[side] += matchsticks[i]
                    
                    if backtrack(i+1): return True
                    sides[side] -= matchsticks[i]
            return False
        
        # start index 0
        return backtrack(0)
'''
Time Complexity: 
Space Complexity: 

refer to: https://www.youtube.com/watch?v=hUe0cUKV-YY
'''