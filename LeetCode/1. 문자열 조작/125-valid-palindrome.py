# https://leetcode.com/problems/valid-palindrome/

# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()   # 소문자 변환
        s = re.sub('[^a-z0-9]', '', s)  # 문자 필터링

        return s == s[::-1]