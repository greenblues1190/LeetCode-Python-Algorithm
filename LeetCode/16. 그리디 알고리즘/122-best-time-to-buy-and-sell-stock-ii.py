# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).

# Constraints:

# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                result += profit
        return result
