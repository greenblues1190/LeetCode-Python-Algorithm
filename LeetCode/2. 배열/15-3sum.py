# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        length = len(nums)

        for i in range(length - 2):
            # 중복 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            complement = -1 * nums[i]

            # 투포인터를 좁혀가며 sum 계산
            left, right = i + 1, length - 1
            while left < right:
                # sum이 -1 * nums[i]이면 result에 추가
                sum = nums[left] + nums[right]
                if sum < complement:
                    left += 1
                elif sum > complement:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 중복 스킵
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result