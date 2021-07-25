# https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively,return the minimum window substring
# of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.


import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1
            
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                    
                if not end or (right - left <= end - start):
                    start, end = left, right

        return s[start:end]