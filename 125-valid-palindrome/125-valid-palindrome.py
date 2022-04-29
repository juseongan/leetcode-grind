class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1 # left and right pointers starting at each end
        
        while l < r: # go through the string before the pointers meet or cross each other
            while l < r and not s[l].isalnum(): # check for non-alphanumeric characters
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower(): # compare the letters in lowercase
                return False
            
            l += 1 # move the pointers
            r -= 1
        
        return True