# https://leetcode.com/problems/majority-element/

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -231 <= nums[i] <= 231 - 1


from typing import List


# use sorting
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]