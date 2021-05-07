# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}    # dictionary 생성
        
        # dictionary에 nums의 인덱스와 값을 바꿔 저장
        for i, num in enumerate(nums):
            map[num] = i
        
        # nums를 순회하며 target에서 원소를 뺀 값을 dictionary에서 검색
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map and i != map[complement]:
                return [i, map[complement]]