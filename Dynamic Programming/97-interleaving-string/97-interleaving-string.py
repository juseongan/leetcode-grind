# Recursive function with memoization
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        L1, L2, L3 = len(s1), len(s2), len(s3)
        visited = set()
        
        def interleavingString(idx1, idx2, idx3):
            if idx1 == L1 and idx2 == L2 and idx3 == L3:
                return True
            
            a, b = False, False
            
            if idx1 < L1 and idx3 < L3:
                if s1[idx1] == s3[idx3]:
                    if (idx1+1,idx2,idx3+1) not in visited:
                        visited.add((idx1+1, idx2, idx3+1))
                        a = interleavingString(idx1+1, idx2, idx3+1)
            if idx2 < L2 and idx3 < L3:
                if s2[idx2] == s3[idx3]:
                    if (idx1, idx2+1, idx3+1) not in visited:
                        visited.add((idx1, idx2+1, idx3+1))
                        b = interleavingString(idx1, idx2+1, idx3+1)        
            return a or b
            
        if interleavingString(0, 0, 0):
            return True
        return False

# Using dynamic programming with a queue and memoization
import collections

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        L1, L2, L3 = len(s1), len(s2), len(s3)
        
        queue = collections.deque([(0, 0, 0)])
        
        visited = set()
        
        while queue:
            idx1, idx2, idx3 = queue.popleft()
            
            if (idx1, idx2, idx3) in visited:
                continue
            visited.add((idx1, idx2, idx3))
            
            if idx1==L1 and idx2==L2 and idx3==L3:
                return True
            
            if idx1<L1 and idx3<L3:
                if s1[idx1]==s3[idx3]:
                    queue.append((idx1+1, idx2, idx3+1))
            if idx2<L2 and idx3<L3:
                if s2[idx2]==s3[idx3]:
                    queue.append((idx1, idx2+1, idx3+1))
        return False


# Recursion(dfs) with cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = {}
        def dfs(i1, i2):
            if i1 == len(s1) and i2 == len(s2):
                return True
            if (i1, i2) in dp:
                return dp[(i1,i2)]
            
            if i1 < len(s1) and s1[i1] == s3[i1+i2] and dfs(i1+1, i2):
                return True
            if i2 < len(s2) and s2[i2] == s3[i1+i2] and dfs(i1, i2+1):
                return True
            
            dp[(i1, i2)] = False
            return False
        
        return dfs(0, 0)