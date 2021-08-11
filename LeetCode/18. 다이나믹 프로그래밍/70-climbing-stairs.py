# https://leetcode.com/problems/climbing-stairs/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways
# can you climb to the top?

# Constraints:

# 1 <= n <= 45


import collections


# memoization, since it's same solution of fibonacci.
class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]


# save memory
class Solution:
    dp = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:
        x = 0
        y = 1
        
        for i in range(n):
            x, y = y, x + y
            
        return y