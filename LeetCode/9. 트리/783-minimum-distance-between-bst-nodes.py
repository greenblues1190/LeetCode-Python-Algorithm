# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Given the root of a Binary Search Tree (BST), return the minimum difference
# between the values of any two different nodes in the tree.


import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# resulsively inorder search
class Solution:
    prev_val = -sys.maxsize
    min_diff = sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        # search tree inorder: left child - root - right child
        if root.left:
            self.minDiffInBST(root.left)

        self.min_diff = min(self.min_diff, root.val - self.prev_val)
        self.prev_val = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.min_diff
