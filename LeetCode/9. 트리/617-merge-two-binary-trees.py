# https://leetcode.com/problems/merge-two-binary-trees/

# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.
# You need to merge the two trees into a new binary tree.
# The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.


import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Reculsive
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            merged_root = TreeNode(root1.val + root2.val)
            merged_root.left = self.mergeTrees(root1.left, root2.left)
            merged_root.right = self.mergeTrees(root1.right, root2. right)
            return merged_root
        else:
            return root1 or root2


# BFS
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None and root2 is None:
            return None
        elif root1 is None:
            return root2
        elif root2 is None:
            return root1

        queue = collections.deque()
        queue.append((root1, root2))

        while queue:
            node1, node2 = queue.popleft()
            node1.val += node2.val

            if node1.left and node2.left:
                queue.append((node1.left, node2.left))
            if node1.right and node2.right:
                queue.append((node1.right, node2.right))

            if node1.left is None:
                node1.left = node2.left
            if node1.right is None:
                node1.right = node2.right

        return root1
