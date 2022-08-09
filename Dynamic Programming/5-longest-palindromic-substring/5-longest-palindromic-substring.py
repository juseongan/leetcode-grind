# Two pointer
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right -1]:
                left -= 1
                right += 1
            return s[left +1: right -1]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''
        
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1),expand(i, i+2), key=len)
        return result


# Dynamic Programming
'''
Time complexity O(n^3)
                O(n^2): Brute Force
                O(n): Check if a string is a palindromic or not.
'''
