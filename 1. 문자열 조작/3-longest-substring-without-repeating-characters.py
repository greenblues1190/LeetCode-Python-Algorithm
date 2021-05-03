# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_length = len(s)

        def expand(left: int) -> int:
            right = left
            while right < string_length and s[right] not in s[left:right]:
                right += 1
            return right - left

        if string_length < 2:
            return string_length

        result = 1
        for i in range(0, string_length - 1):
            result = max(result, expand(i))

        return result
