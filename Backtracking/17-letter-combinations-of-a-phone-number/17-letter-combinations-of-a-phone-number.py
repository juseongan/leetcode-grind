# Hyochan's solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        self.output = []
        self.key = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'} 
        self.N = len(digits)
        
        def letter_combinations(string, numbers):
            if numbers:
                letters = self.key[numbers[0]]
                for i in range(len(letters)):
                    letter = letters[i]
                    string += letter
                    if len(string) == self.N:
                        self.output.append(string)
                    else:
                        letter_combinations(string, numbers[1:])
                    string = string[:-1]
        
        letter_combinations("", digits)
        
        return self.output

# Hyebin's solution
# dfs -> backtracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # represent telephone buttons to graph
        buttons = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        if not digits: 
            return [] # if digits is "", return []
        
        combinations = []
        def dfs(combination, i):
            # 종료 조건
            if len(combination) == len(digits):
                combinations.append(combination)
                return
            
            for i in range(i, len(digits)): # i is index of digits
                number = digits[i]
                strings = buttons[number]
                for string in strings:
                    dfs(combination+string, i+1)    
                
        dfs("", 0)
        return combinations