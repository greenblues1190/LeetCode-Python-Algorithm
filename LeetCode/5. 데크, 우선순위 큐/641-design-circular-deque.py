# https://leetcode.com/problems/design-circular-deque/

# Design your implementation of the circular double-ended queue (deque).

# Your implementation should support following operations:
# MyCircularDeque(k): Constructor, set the size of the deque to be k.
# insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
# insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
# deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
# deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
# getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
# getRear(): Gets the last item from Deque. If the deque is empty, return -1.
# isEmpty(): Checks whether Deque is empty or not.
# isFull(): Checks whether Deque is full or not.

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.left = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.head = self.tail = prev_node = ListNode()
        for _ in range(k - 1):
            new_node = ListNode()
            prev_node.right = new_node
            new_node.left = prev_node
            prev_node = new_node
        prev_node.right = self.head
        self.head.left = prev_node

    def insertFront(self, value: int) -> bool:
        if self.head.val is None:
            self.head.val = value
            return True
        elif self.head.left.val is None:
            self.head.left.val = value
            self.head = self.head.left
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.tail.val is None:
            self.tail.val = value
            return True
        elif self.tail.right.val is None:
            self.tail.right.val = value
            self.tail = self.tail.right
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.head.val is None:
            return False
        else:
            self.head.val = None
            if self.head.right.val is not None:
                self.head = self.head.right
            return True

    def deleteLast(self) -> bool:
        if self.tail.val is None:
            return False
        else:
            self.tail.val = None
            if self.tail.left.val is not None:
                self.tail = self.tail.left
            return True

    def getFront(self) -> int:
        if self.head.val is None:
            return -1
        else:
            return self.head.val

    def getRear(self) -> int:
        if self.tail.val is None:
            return -1
        else:
            return self.tail.val

    def isEmpty(self) -> bool:
        if self.head == self.tail and self.head.val is None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.head.left == self.tail:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
