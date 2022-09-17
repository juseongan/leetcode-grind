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
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
         
        letter = {
            "2": "abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                for j in letter[digits[i]]:
                    dfs(i+1, path+j)
                    
        if not digits:
            return []
        
        
        result = []
        dfs(0, "")
        
        return result