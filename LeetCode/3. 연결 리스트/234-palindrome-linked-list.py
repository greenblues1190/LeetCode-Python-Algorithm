# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.

# from typing import Deque
# import collections


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: Deque = collections.deque()

        if not head:
            return True

        # ListNode를 list로 변환
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True
