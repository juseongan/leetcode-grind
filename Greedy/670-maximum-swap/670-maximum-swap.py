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