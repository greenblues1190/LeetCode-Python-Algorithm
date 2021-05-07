# https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Solve it in O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        for i in range(len(nums)):
            result.append(product)
            product *= nums[i]

        product = 1
        for i in range(len(nums)-1, 0):
            result[i] *= product
            product *= nums[i]

        return result