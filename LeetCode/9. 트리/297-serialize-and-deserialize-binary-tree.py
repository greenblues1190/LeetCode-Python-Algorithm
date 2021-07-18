# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Serialization is the process of converting a data structure or object into
# a sequence of bits so that it can be stored in a file or memory buffer,
# or transmitted across a network connection link to be reconstructed later
# in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string
# and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format,
# so please be creative and come up with different approaches yourself.


import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        string = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                string.append(str(node.val))
            else:
                string.append("#")
        serialized = ','.join(string)
        return serialized

    def deserialize(self, data: str) -> TreeNode:
        if data[0] == "#":
            return None

        parsed = data.split(",")
        root = TreeNode(int(parsed[0]))
        queue = collections.deque([root])

        i = 1
        while queue:
            parent_node = queue.popleft()

            if parent_node and i < len(parsed):
                left_node = right_node = None
                if parsed[i] != "#":
                    parent_node.left = TreeNode(int(parsed[i]))
                    queue.append(parent_node.left)

                if parsed[i + 1] != "#":
                    parent_node.right = TreeNode(int(parsed[i + 1]))
                    queue.append(parent_node.right)

                i += 2

        return root
