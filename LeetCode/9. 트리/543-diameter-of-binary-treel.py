# https://leetcode.com/problems/diameter-of-binary-tree/

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            self.max_diameter = max(self.max_diameter, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.max_diameter
