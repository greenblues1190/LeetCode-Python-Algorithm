# https: // leetcode.com/problems/kth-largest-element-in-an-array/

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.


from typing import List
import heapq


# sort list
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


# use heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        answer = 0
        max_heap = list()

        for num in nums:
            heapq.heappush(max_heap, -num)

        for _ in range(k):
            answer = heapq.heappop(max_heap)

        return -answer
