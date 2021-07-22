# https://leetcode.com/problems/intersection-of-two-arrays/

# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.


from typing import List


# use two-pointer
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        intersection = set()

        pos1 = pos2 = 0

        while pos1 < len(nums1) and pos2 < len(nums2):
            if nums1[pos1] > nums2[pos2]:
                pos2 += 1
            elif nums1[pos1] < nums2[pos2]:
                pos1 += 1
            else:
                intersection.add(nums1[pos1])
                pos1 += 1
                pos2 += 1

        return intersection


# use binary search
class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()

        intersection = set()

        for n1 in nums1:
            if self.binary_search(nums2, n1) != -1:
                intersection.add(n1)

        return intersection
