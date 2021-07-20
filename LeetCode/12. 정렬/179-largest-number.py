# https://leetcode.com/problems/largest-number/

# Given a list of non-negative integers nums, arrange them such that they form the largest number.

# Note: The result may be very large, so you need to return a string instead of an integer.


from typing import List


class Solution:
    def _compare(self, num1: int, num2: int) -> bool:
        str1 = str(num1)
        str2 = str(num2)
        return str1 + str2 < str2 + str1

    def largestNumber(self, nums: List[int]) -> str:        
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self._compare(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j = j - 1
            i += 1

        return str(int(''.join([str(num) for num in nums])))
