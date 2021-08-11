# https://leetcode.com/problems/fibonacci-number/

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Constraints:

# 0 <= n <= 30


import collections


# memoization (bottom-up)
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]


# tabulation (top-down)
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]

        return self.dp[n]



# save memory
class Solution:
    def fib(self, n: int) -> int:
        x = 0
        y = 1
        
        for i in range(0, n):
            x, y = y, x + y
            
        return x