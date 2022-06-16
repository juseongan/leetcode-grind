class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        palinLen = 0
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > palinLen:
                    palindrome = s[l:r+1]
                    palinLen = r - l + 1
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > palinLen:
                    palindrome = s[l:r+1]
                    palinLen = r - l + 1
                l -= 1
                r += 1
                
        return palindrome