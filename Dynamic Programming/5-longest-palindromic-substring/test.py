class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Declare variables
        max_palindormic_length = 0
        dp = [[0]*len(s) for _ in range(len(s))]
        


        # Base case
        if len(s) < 2: return print(s)



        # Obtain longest palindrome string's length
        for i in range(len(s)-1, -1, -1):  # from s[last_index] to s[first_index]
            for j in range(i, len(s), 1):         

                # Case1. i == j
                if i == j and s[i] == s[j]: 
                    dp[i][j] = 1           # == dp[i][i]
                    #max_palindormic_length = max(max_palindormic_length, dp[i][j])

                # Case2. i+1 == j
                elif i+1 == j and s[i] == s[j]: 
                    dp[i][j] = 2           # = dp[i][i] + 1
                    #max_palindormic_length = max(max_palindormic_length, dp[i][j])

                # Case3. i+1 < j
                elif dp[i+1][j-1] > 0 and s[i] == s[j]: 
                        dp[i][j] = dp[i+1][j-1] + 2
                        #max_palindormic_length = max(max_palindormic_length, dp[i][j])
                        #start_index = i

                # Case4. i > j or s[i] != s[j]
                else: continue

        # Obtain answer
        print(dp)


s = "aacabdkacaa"
solution = Solution()
solution.longestPalindrome(s)