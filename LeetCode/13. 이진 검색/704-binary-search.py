# https://leetcode.com/problems/binary-search/

# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


from typing import List


# reculsive
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right) -> int:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if left >= right:
                return -1

            if nums[mid] > target:
                index = binary_search(left, mid - 1)
            else:
                index = binary_search(mid + 1, right)

            return index

        return binary_search(0, len(nums) - 1)


# iterative
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1
