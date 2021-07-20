# https://leetcode.com/problems/sort-list/

# Given the head of a linked list, return the list after sorting it in ascending order.

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    # merge sort
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        # find middle node using runner technique
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # reculsively divide list
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        # merge divided two lists
        return self.mergeTwoLists(l1, l2)
