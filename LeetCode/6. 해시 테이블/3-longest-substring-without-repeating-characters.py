# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strlength = len(s)
        max_length = 0
        
        def expand(left: int) -> int:
            right = left = i
            while right < strlength and s[right] not in s[left:right]:
                right += 1
            if left == right:
                return 1
            return right - left
        
        for i in range(0, strlength):
            max_length = max(max_length, expand(i))
            
        return max_length