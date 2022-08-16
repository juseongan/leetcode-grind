num = 9973

# Convert int -> list
num = list(str(num))

# Find Min, Max in num
if num[0] != max(num):
    num_max = num.index(max(num))
    num_min = num.index(min(num)) 

    num[num_max], num[num_min] = num[num_min], num[num_max]

else:    
    for i in range(len(num)-1):
        if num[i+1] > num[i]:
                temp = num[i+1]
                num[i+1] = num[i]
                num[i] = temp
                break





# Convert list -> str -> int
num = "".join(num)
num = int(num)

# Return int
print(num)

class Solution:
    # Author: juseongan
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maximumSwap(self, num: int) -> int:
        numList = [int(char) for char in str(num)]
        
        max_idx = len(numList) - 1
        earliest = latest = 0
        for idx in range(len(numList)-1, -1, -1):
            if numList[idx] > numList[max_idx]:     # update the max since current value is larger
                max_idx = idx
            elif numList[idx] < numList[max_idx]:   # switch the max with the earliest int possible
                earliest = idx
                latest = max_idx
            
        numList[earliest], numList[latest] = numList[latest], numList[earliest]
        return int("".join([str(digit) for digit in numList]))