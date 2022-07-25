class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isValid(self, s: str) -> bool:
        bracketMap = { ')':'(', '}':'{', ']':'[' }
        
        bracketStack = [] # keep track of opening brackets
        for char in s:
            if char in bracketMap: # char is a closing bracket
                if bracketStack and bracketStack[-1] == bracketMap[char]: # stack isn't empty and top matches opening bracket
                    bracketStack.pop()
                
                else:
                    return False
            
            else: # char is a opening bracket
                bracketStack.append(char)
            
        return not bracketStack # return True if stack is empty