# https://leetcode.com/problems/combination-sum/

# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target
# is less than 150 combinations for the given input.


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(start, combination=[]):
            sum_combination = sum(combination)

            if sum_combination > target or len(combination) >= 150:
                return
            if sum_combination == target:
                # print(sum_combination, ":", combination)
                result.append(combination[:])
                return

            for i in range(start, len(candidates)):
                dfs(i, combination + [candidates[i]])

            return

        dfs(0)
        return result
