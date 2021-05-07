# https: // leetcode.com/problems/reverse-linked-list-ii/

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 예외 처리
        if not head or left == right:
            return head

        root = start = ListNode()
        root.next = head

        # start : left 바로 전, end : left 시작 지점
        # start와 left는 끝날 때까지 값이 변하지 않음
        for _ in range(left - 1):
            start = start.next
        end = start.next

        # swap
        for _ in range(right - left):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp

        return root.next
