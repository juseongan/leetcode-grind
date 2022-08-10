class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = [] # bottom -> stack[0], top -> stack[-1]
        
        for c in s:
            if c == ')':
                if len(stack) > 0:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(c)
                else:
                    stack.append(c)
            else:
                stack.append(c)
        
        return len(stack)