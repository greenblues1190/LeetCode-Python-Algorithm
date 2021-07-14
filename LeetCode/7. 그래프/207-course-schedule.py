# https://leetcode.com/problems/course-schedule/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi]
# indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.


from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(start: int) -> bool:
            # if cycle is detected, return false
            if start in visited:
                return False
            if start in valid_courses:
                return True

            # search next course
            visited.add(start)
            for next_course in list(graph[start]):
                if dfs(next_course) == False:
                    return False

            # if there's no cycle, delete all the visted nodes in discovered
            visited.remove(start)
            valid_courses.add(start)
            return True

        # convert prerequisites into graph
        graph = defaultdict(list)
        for prerequisite, course in prerequisites:
            graph[prerequisite].append(course)
        # use set because it's faster for item check, O(1)
        visited = set()
        valid_courses = set()

        for course in range(numCourses):
            if dfs(course) == False:
                return False

        return True
