# https://leetcode.com/problems/reconstruct-itinerary/

# You are given a list of airline tickets where
# tickets[i] = [fromi, toi] represent the departure
# and the arrival airports of one flight.
# Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs
# from "JFK", thus, the itinerary must begin with "JFK".
# If there are multiple valid itineraries, you should
# return the itinerary that has the smallest lexical order
# when read as a single string.

# For example, the itinerary ["JFK", "LGA"]
# has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary.
# You must use all the tickets once and only once.


from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(graph: dict, start: str, route=[]) -> List[List[str]]:
            while graph[start]:
                route = dfs(graph, graph[start].pop(), route)
            route.append(start)
            return route

        graph = defaultdict(list)
 
        for departure, arrival in sorted(tickets, reverse=True):
            graph[departure].append(arrival)
            
        return dfs(graph, "JFK")[::-1]