class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        s = s[s.find("1"):]
        s = s[:s.rfind("0")+1]
        if len(s) == 0:
            return 0
        
        # Initialize the dp table
        dp = [[0],[0]]
        
        # Create the dp table
        L = len(s)
        row, cnt = 0, 1
        for idx in range(L-1):
            if s[idx] != s[idx+1]:
                dp[row].append(cnt)
                row = (row + 1) % 2
                cnt = 1
            else:
                cnt += 1
        dp[row].append(cnt)
        
        # Make the dp table into a dp sum table
        N = len(dp[0])
        for j in range(1,N):
            dp[0][j] += dp[0][j-1]
            dp[1][j] += dp[1][j-1]
        
        # Calculate the answer
        flips = 100001
        for j in range(N):
            flips = min(flips, dp[1][N-1] - dp[1][j] + dp[0][j])
        return flips

# Prefix Sum Approach
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        numFlips = 0                            # intially both are 0
        numOnes = 0
        
        for c in range(len(s)):                 # if not 1 then it's a zero
            if (s[c] == "1"):
                numOnes += 1
            elif (numOnes > 0):
                numFlips += 1                   # in case we have already seen a zero, we will increase the numFlips
            numFlips = min(numFlips, numOnes)   # we will do a fip if its count is less then # of 1's seen so far
            
        return numFlips