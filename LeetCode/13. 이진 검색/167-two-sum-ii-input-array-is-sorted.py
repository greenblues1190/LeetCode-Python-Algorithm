# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Given an array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2,
# where 1 <= answer[0] < answer[1] <= numbers.length.

# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.


from typing import List


# binary search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx1, num1 in enumerate(numbers):
            left, right = idx1 + 1, len(numbers) - 1
            expected = target - num1
            while left <= right:
                mid = left + (right - left) // 2

                if numbers[mid] > expected:
                    right = mid - 1
                elif numbers[mid] < expected:
                    left = mid + 1
                else:
                    return idx1 + 1, mid + 1


# two-pointer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left != right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return left + 1, right + 1