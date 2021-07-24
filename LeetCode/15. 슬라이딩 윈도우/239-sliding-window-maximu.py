# https://leetcode.com/problems/sliding-window-maximum/


# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can only
# see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.


from typing import List
import collections


# use queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = collections.deque()
        currentmax = float('-inf')

        for i, num in enumerate(nums):
            window.append(num)

            if i < k - 1:
                continue

            if currentmax == float('-inf'):
                currentmax = max(window)
            elif currentmax < num:
                currentmax = num

            result.append(currentmax)

            if currentmax == window.popleft():
                currentmax = float('-inf')

        return result
