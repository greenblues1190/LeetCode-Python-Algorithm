# https://leetcode.com/problems/task-scheduler/

# Given a characters array tasks, representing the tasks a CPU needs to do,
# where each letter represents a different task. Tasks could be done in any order.
# Each task is done in one unit of time. For each unit of time, the CPU could
# complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period
# between two same tasks (the same letter in the array), that is that there must
# be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all
# the given tasks.

# Constraints:

# 1 <= task.length <= 104
# tasks[i] is upper-case English letter.
# The integer n is in the range [0, 100].


from typing import List
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        result = 0
        count = collections.Counter(tasks)

        while True:
            sub_count = 0
            for task, _ in count.most_common(n + 1):
                # execute n + 1 tasks
                sub_count += 1
                result += 1
                count.subtract(task)
                # remove items which is its frequency is less than 1
                count += collections.Counter()

            if not count:
                break

            result += n - sub_count + 1
