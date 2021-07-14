# https://leetcode.com/problems/combinations/

# Given two integers n and k, return all possible
# combinations of k numbers out of the range [1, n].

# You may return the answer in any order.


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start: int, k: int, combination=[], result=[]) -> List[List[int]]:
            if k == 0:
                result.append(combination[:])
                return result
            
            for i in range(start, n + 2 - k):
                combination.append(i)
                result = dfs(i + 1, k - 1, combination, result)
                combination.pop()
                
            return result
        
        return dfs(1, k)