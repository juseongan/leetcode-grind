# Juseong's solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(idx, combination):
            # if the path is the same length as digits, we have a complete combination
            if len(combination) == len(digits):
                combinations.append(combination)
                return
            
            # loop through all the possible letters
            for letter in letterMap[digits[idx]]:
                backtrack(idx + 1, combination + letter)
            
        combinations = []
        if digits:
            backtrack(0, "")
            
        return combinations

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
        
        # represents telephone buttons to graph
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
            return [] # if digits are "", return []
        
        combinations = []
        def dfs(combination, index):
            # If I combine each digit of 'digits', I will store the result of combining and backtrack
            if len(combination) == len(digits):
                combinations.append(combination)
                return
            
            # Access each element of 'digits'
            # If i write 'for digit in digits' -> we can not move to next index's string. because 'str' can concatenate only 'str'
            # so I will use 'index'
            # Let the first element's index of 'digits' be i
            # 1 character of the 'i'th string and concatenates each charater in the 'i+1'th string
            for i in range(index, len(digits)): # you can write 'index' as 'i'.
                digit = digits[i]
                strings = buttons[digit]
                for string in strings:
                    # If the i-th character is picked, the search begins
                    dfs(combination+string, i+1)    
                
        dfs("", 0)
        return combinations