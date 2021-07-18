# https://leetcode.com/problems/maximum-erasure-value/

# You are given an array of positive integers nums and want to erase a subarray
# containing unique elements. The score you get by erasing the subarray is
# equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguoussubsequence
# of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).


from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = 0
        left = right = 0
        subarray = {}
        while right < len(nums):
            if nums[right] not in subarray:
                subarray[nums[right]] = right
                current_sum += nums[right]
                right += 1
                max_sum = max(max_sum, current_sum)
            else:
                del subarray[nums[left]]
                current_sum -= nums[left]
                left += 1
        return max_sum