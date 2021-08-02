# https://leetcode.com/problems/different-ways-to-add-parentheses/

# Given a string expression of numbers and operators, return all possible results
# from computing all the different possible ways to group numbers and operators.
# You may return the answer in any order.

# Constraints:

# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.


from typing import List


class Solution:
    def compute(self, left, right, operation) -> int:
        result = []

        for l in left:
            for r in right:
                result.append(eval(str(l) + operation + str(r)))

        return result

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        result = []
        for index, value in enumerate(expression):
            if value in "+-*":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])
                result.extend(self.compute(left, right, value))

        return result
