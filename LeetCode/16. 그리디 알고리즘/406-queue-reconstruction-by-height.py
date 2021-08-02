# https://leetcode.com/problems/queue-reconstruction-by-height/

# You are given an array of people, people, which are the attributes of some people
# in a queue (not necessarily in order). Each people[i] = [hi, ki] represents
# the ith person of height hi with exactly ki other people in front who have
# a height greater than or equal to hi.

# Reconstruct and return the queue that is represented by the input array people.
# The returned queue should be formatted as an array queue, where queue[j] = [hj, kj]
# is the attributes of the jth person in the queue (queue[0] is the person at the
# front of the queue).

# Constraints:
x
# 1 <= people.length <= 2000
# 0 <= hi <= 106
# 0 <= ki < people.length
# It is guaranteed that the queue can be reconstructed.


from typing import List
import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        result = []

        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])

        return result
