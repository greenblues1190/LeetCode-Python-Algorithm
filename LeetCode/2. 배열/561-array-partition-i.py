# https://leetcode.com/problems/array-partition-i/

# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 짝수번째 원소들의 합
        return sum(sorted(nums)[::2])
