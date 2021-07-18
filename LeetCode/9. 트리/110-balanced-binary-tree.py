# https://leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ
# in height by no more than 1.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root: TreeNode) -> int:
            if root is None:
                return 0

            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
                return -1
            else:
                return max(left_depth, right_depth) + 1

        return dfs(root) != -1
