# Recursion Approach
class Solution:
    # Time Complexity: O(2^n) exponential time
    # Space Complexity: O(n)
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)

# Bottom-Up Approach with Tabulation
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        
        cache = [0] * (N + 1)
        cache[1] = 1
        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[N]

# Top-Down Approach with Memoization
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    cache = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]