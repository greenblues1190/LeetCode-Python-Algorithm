# https://leetcode.com/problems/network-delay-time/

# You are given a network of n nodes, labeled from 1 to n.
# You are also given times, a list of travel times as
# directed edges times[i] = (ui, vi, wi), where ui is the source node,
# vi is the target node, and wi is the time it takes
# for a signal to travel from source to target.

# We will send a signal from a given node k.
# Return the time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.


from typing import List
import heapq
import sys
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))

        def dijkstra(graph: list, node_num: int, start: int) -> dict:
            min_times = {i: sys.maxsize for i in range(1, node_num + 1)}
            min_times[start] = 0

            queue = []
            heapq.heappush(queue, (0, start))

            while queue:
                weight, node = heapq.heappop(queue)

                for next_node, next_weight in graph[node]:
                    next_time = weight + next_weight
                    if next_time < min_times[next_node]:
                        min_times[next_node] = next_time
                        heapq.heappush(queue, (next_time, next_node))

            return min_times

        result = max(dijkstra(graph, n, k).values())
        if result == sys.maxsize:
            return -1
        return result
