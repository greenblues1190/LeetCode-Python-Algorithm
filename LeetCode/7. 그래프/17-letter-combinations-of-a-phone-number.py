# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
# Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons)
# is given below. Note that 1 does not map to any letters.


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index: int, path: str = "", result: List[str] = []) -> List[str]:
            if len(path) == len(digits):
                result.append(path)
                return result

            for i in range(index, len(digits)):
                for j in keypad[digits[i]]:
                    result = dfs(i + 1, path + j, result)

            return result

        if not digits:
            return []

        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        return dfs(0)
