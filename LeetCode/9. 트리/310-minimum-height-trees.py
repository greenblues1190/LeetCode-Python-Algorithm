# https://leetcode.com/problems/minimum-height-trees/

# A tree is an undirected graph in which any two vertices are connected by exactly
# one path. In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
# where edges[i] = [ai, bi] indicates that there is an undirected edge between
# the two nodes ai and bi in the tree, you can choose any node of the tree as the root.
# When you select a node x as the root, the result tree has height h.
# Among all possible rooted trees, those with minimum height (i.e. min(h))
# are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path
# between the root and a leaf.


from typing import List
import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return range(n)

        # convert edges to graph
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # find inital leaves
        leaves = []
        for key in range(n):
            if len(graph[key]) == 1:
                leaves.append(key)

        # remove leaves until nodes less than 2 left
        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

                leaves = new_leaves

        return leaves
