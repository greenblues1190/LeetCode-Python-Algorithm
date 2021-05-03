# https://leetcode.com/problems/palindromic-substrings/

# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

class Solution:
    def countSubstrings(self, s: str) -> int:
        string_length = len(s)

        def expand(left: int, right: int) -> int:
            temp_count = 0
            while left >= 0 and right < string_length and s[left] == s[right]:
                left -= 1
                right += 1
                temp_count += 1
            return temp_count

        count = string_length
        for i in range(0, string_length - 1):
            count += expand(i, i + 1) + expand(i, i + 2)

        return count