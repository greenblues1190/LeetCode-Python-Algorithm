# https://leetcode.com/problems/number-of-1-bits/

# Write a function that takes an unsigned integer and returns the number of '1' bits it has
# (also known as the Hamming weight).

# Note:

# Note that in some languages, such as Java, there is no unsigned integer type.
# In this case, the input will be given as a signed integer type. It should not affect your implementation,
# as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation.
# Therefore, in Example 3, the input represents the signed integer. -3.

# The input must be a binary string of length 32.


# use count
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


# use bitwise operation
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            n &= n - 1
            count += 1
        return count
    