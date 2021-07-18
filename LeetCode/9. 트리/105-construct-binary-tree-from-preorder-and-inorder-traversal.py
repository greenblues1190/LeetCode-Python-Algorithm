# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same tree,
# construct and return the binary tree.


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        
        root_index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[root_index])
        
        root.left = self.buildTree(preorder, inorder[0:root_index])
        root.right = self.buildTree(preorder, inorder[root_index + 1:])
        
        return root
