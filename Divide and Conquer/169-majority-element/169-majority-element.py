'''
Explan how to solve
1. Count each element occurrences
2. Find the element occurrences appears more than len(nums)//2 times
3. Return 
'''
# Brute Force (using built-in function) -> Time Limit Exceeded!
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        '''
        모든 요소를 카운트하여 조건에 부합하는지 확인
        1. count함수 사용
        2. len(nums)//2 (=n)보다 큰지 비교
        '''
        for num in nums:
            if nums.count(num) > len(nums) // 2: # count(x): Return the number of times x appears in the list.
                return num
'''
Time Complexity: O(n^2)
Space Complexity: O(1)
'''



# Hash map
'''
Hash map allows me to count element occurrences efficiently.

Algorithm
1. maps elements to counts -> count occurrences linear time by looping over nums.
2. return the key with maximum value.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counts = collections.Counter(nums)
        
        return max(counts.keys(), key=counts.get) # .keys(): Returns a view object. 
'''
Time Complexity: T(n(iterate over nums) + c(insertion on each iteration)) -> O(n)
Space Complexity: O(n): At most, the Hash map can contain n - (n/2) associations.
'''



# Divide and Conquer
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Base case
        if len(nums)==1:
            return nums[0]
        
        # Divide 
        half = len(nums)//2 # Declaring half is faster than 3 times len(nums)//2
        left = self.majorityElement(nums[:half])   
        right = self.majorityElement(nums[half:])
        
        # Conquer
        '''
        temp = [right][left]
        if nums.count(left) > half:
            return temp[1]
        else:
            return temp[0]
        '''
        return [right, left][nums.count(left)>half] # Use this expression to reduce Space comeplexity 
'''
Time Complexity: 
Space Complexity: 
'''



# Dynamic Programming
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dp_counts = collections.defaultdict(int)
        
        for num in nums:
            
            # 계산 결과 저장
            if dp_counts[num] == 0:
                dp_counts[num] = nums.count(num)
                
            # 저장된 값 사용
            if dp_counts[num] > len(nums)//2:
                return num
'''
Time Complexity: O(n)
Space Complexity: O(n)
'''




# Pythonic way
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        '''
        nums 배열에는 항상 majority element(: len(nums)/2 번 등장하는 요소)가 존재
        '''
        return sorted(nums)[len(nums)//2] # Return sorted list
'''
Time Complexity: O(nlogn)
Space Complexity: O(n)

* nums.sort()[len(num)//2] -> TypeError!
'NoneType' object is not subscriptable.
'''