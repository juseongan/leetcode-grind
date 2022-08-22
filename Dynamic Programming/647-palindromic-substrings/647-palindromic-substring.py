class Solution:
    def countSubstrings(self, s: str) -> int:        
        def checkPalindrome(left, right) -> int:
            num_palindromes = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                num_palindromes += 1
                left -= 1
                right += 1
            return num_palindromes

        result = 0
        for idx in range(len(s)):
            result += checkPalindrome(idx, idx) # check for odd lengthed palindromes
            result += checkPalindrome(idx, idx+1) # check for even lengthed palindromes

        return result
