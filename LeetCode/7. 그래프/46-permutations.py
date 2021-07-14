# https://leetcode.com/problems/permutations/

# Given an array nums of distinct integers,
# return all the possible permutations.
# You can return the answer in any order.


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(array: List[int], permutation=[], result=[]) -> List[List[int]]:
            if len(array) == 0:
                result.append(permutation[:])
                return result

            for elem in array:
                next_array = array[:].remove(elem)
                permutation.append(elem)
                result = dfs(next_array, permutation, result)
                permutation.pop()

            return result

        return dfs(nums)
