# https://leetcode.com/problems/merge-intervals/


# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the
# non-overlapping intervals that cover all the intervals in the input.


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if merged and interval[0] <= merged[-1][1]:
                # if intervals overlaps
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                # or not
                merged += interval,
        return merged
