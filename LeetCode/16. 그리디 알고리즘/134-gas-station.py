# https://leetcode.com/problems/gas-station/

# There are n gas stations along a circular route, where the amount of gas
# at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
# from the ith station to its next (i + 1)th station. You begin the journey with
# an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index
# if you can travel around the circuit once in the clockwise direction, otherwise
# return -1. If there exists a solution, it is guaranteed to be unique

# Constraints:

# gas.length == n
# cost.length == n
# 1 <= n <= 104
# 0 <= gas[i], cost[i] <= 104


from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0

        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]

        return start
