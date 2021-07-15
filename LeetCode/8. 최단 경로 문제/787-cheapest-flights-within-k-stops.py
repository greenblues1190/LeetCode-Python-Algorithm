# https://leetcode.com/problems/cheapest-flights-within-k-stops/

# There are n cities connected by some number of flights.
# You are given an array flights where flights[i] = [fromi, toi, pricei]
# indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k,
# return the cheapest price from src to dst with at most k stops.
# If there is no such route, return -1.


from typing import List
import heapq
import collections


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append([v, w])

        queue, traced = [(0, src, k)], dict()

        while queue:
            price, node, remain_stops = heapq.heappop(queue)
            if node == dst:
                return price

            if node in traced and traced[node] >= remain_stops:
                continue
            traced[node] = remain_stops

            if remain_stops >= 0:
                for next_node, next_price in graph[node]:
                    heapq.heappush(queue, (price + next_price,
                                   next_node, remain_stops - 1))

        return -1
