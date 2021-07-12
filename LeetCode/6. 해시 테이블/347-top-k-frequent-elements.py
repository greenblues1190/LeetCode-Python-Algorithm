# https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.


import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in collections.Counter(nums).most_common(k)]