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



# dfs
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        # 전체 둘레로 한 변의 길이가 정수인지 파악
        perimeter = sum(matchsticks) # perimeter is 둘레  
        if perimeter % 4 != 0: return False
        else: side = perimeter // 4  # side is 변
        
        matchsticks.sort(reverse=True)
        # pass the lengths at each side
        def dfs(w,e,n,s,index): # west, east, north, south
            # base case
            # if we find 
            if index==len(matchsticks):
                if w==e==n==s: return True
                return False
            m = matchsticks[index]
            
            '''
            if dfs(w+m,e,n,s,index+1): waste time on 
            '''
            if w+m <= side and dfs(w+m,e,n,s,index+1): return True
            if e+m <= side and dfs(w,e+m,n,s,index+1): return True
            if n+m <= side and dfs(w,e,n+m,s,index+1): return True
            if s+m <= side and dfs(w,e,n,s+m,index+1): return True
            
            return False
        
        return dfs(0,0,0,0,0)
'''
Time Complexity: O(4^n)
Space Complexity: O(n): all the recursive calls.

refer to: https://www.youtube.com/watch?v=Amfd1bqZmVg&t=90s
'''

# Dynamic Programming Approach
class Solution:
    # Time Complexity: O(N * 2^N)
    # Space Complexity: O(N + 2^N)
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        L = len(matchsticks)
        perimeter = sum(matchsticks)
        possible_side =  perimeter // 4

        if possible_side * 4 != perimeter:
            return False

        memo = {}

        def recurse(mask, sides_done):
            total = 0
            for i in range(L - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += matchsticks[L - 1 - i]

            if total > 0 and total % possible_side == 0:
                sides_done += 1
            if sides_done == 3:
                return True
            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]
            
            ans = False

            c = int(total / possible_side)
            rem = possible_side * (c + 1) - total

            for i in range(L - 1, -1, -1):
                if matchsticks[L - 1 - i] <= rem and mask&(1 << i):
                    if recurse(mask ^ (1 << i), sides_done):
                        ans = True
                        break
                        
            memo[(mask, sides_done)] = ans
            return ans
        
        return recurse((1 << L) - 1, 0)