# https://leetcode.com/problems/range-sum-of-bst/

# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0

        if root.val < low:
            value = self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            value = self.rangeSumBST(root.left, low, high)
        else:
            value = root.val + \
                self.rangeSumBST(root.left, low, high) + \
                self.rangeSumBST(root.right, low, high)

        return value
