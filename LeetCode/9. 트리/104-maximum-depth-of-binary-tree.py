# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.


import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, depth=-1) -> int:
            depth += 1
            if root is None:
                return depth
            return max(dfs(root.left, depth), dfs(root.right, depth))
        return dfs(root)


# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def bfs(root: TreeNode) -> int:
            queue = collections.deque([root])
            depth = 0
            while queue:
                depth += 1
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return depth

        return bfs(root)