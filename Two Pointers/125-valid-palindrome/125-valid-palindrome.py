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



'''
Explan how to solve
1. 먼저는 uppercase를 lowercase로 바꾸고 non-alphnumeric characters를 없앤다.
    string_name.lower(), string_name.isalnum()
2. palindrome인지 판별한다.
    2.1 주어진 s 문자열을 reverse 하여 reversed_s에 저장한다.
    2.2 s와 reversed_s가 같은지 비교한다.
3. palindrome이라면 true, 아니라면 false를 반환한다.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # uppercase를 lowercase로 바꾸고 non-alphnumeric characters를 없앤다.
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        
        # palindrome인지 판별한다.
        reversed_s = "".join(reversed(s))
        if s == reversed_s:
            # palindrome이라면 true
            return "true"
        # 아니라면 false를 출력한다.
        else: "false"
        
'''
Time Complexity: T(3n + c) = O(n)
Space Complexity: O(1)

As you can see in the CPython function, there’s no auxiliary space involved and there’s no use of recursion either. Hence the space complexity of the operation is constant i.e O(1).
refer to: https://thecodingbot.com/time-and-space-complexity-analysis-of-pythons-list-reverse-method/#:~:text=Time%20Complexity%3A%20O(N),third%20last%2C%20and%20so%20on.
'''
