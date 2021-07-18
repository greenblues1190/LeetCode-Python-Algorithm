# https://leetcode.com/problems/longest-univalue-path/

# Given the root of a binary tree, return the length of the longest path, where
# each node in the path has the same value. This path may or may not pass through the root.

# The length of the path between two nodes is represented by the number of edges between them.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_length: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if root.left and root.left.val == root.val:
                left += 1
            else:
                left = 0
            if root.right and root.right.val == root.val:
                right += 1
            else:
                right = 0

            self.max_length = max(self.max_length, left + right)

            return max(left, right)

        dfs(root)
        return self.max_length
