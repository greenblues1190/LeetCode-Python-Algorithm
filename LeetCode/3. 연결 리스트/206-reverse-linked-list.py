# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            # next에 다음 노드를 저장, 노드.next에 prev를 저장
            next, node.next = node.next, prev
            # prev에 현재 노드를 저장, 현재 노드에 next 저장
            prev, node = node, next
            print(node)

        return prev 