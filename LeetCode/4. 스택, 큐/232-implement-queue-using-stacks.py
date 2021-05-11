# https: // leetcode.com/problems/implement-queue-using-stacks/

# Implement a first in first out(FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue(push, peek, pop, and empty).

# Implement the MyQueue class:
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:
# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque(double-ended queue) as long as you use only a stack's standard operations.
# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.convert()
        return self.output.pop()

    def peek(self) -> int:
        self.convert()
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []

    def convert(self):
        if not self.output:
            for _ in range(len(self.input)):
                self.output.append(self.input.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
