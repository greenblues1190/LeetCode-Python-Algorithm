# https://leetcode.com/problems/subsets/

# Given an integer array nums of unique elements,
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets.
# Return the solution in any order.


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(start=0, combination=[]) -> None:
            result.append(combination)
            # reculsive search
            for i in range(start, len(nums)):
                dfs(i + 1, combination + [nums[i]])
            return

        dfs()
        return result
