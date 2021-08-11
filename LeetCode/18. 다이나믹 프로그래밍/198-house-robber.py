# https://leetcode.com/problems/house-robber/

# You are a professional robber planning to rob houses along a street. Each house
# has a certain amount of money stashed, the only constraint stopping you from
# robbing each of them is that adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent houses were broken
# into on the same night.

# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400


from typing import List
import collections


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp.popitem()[1]
