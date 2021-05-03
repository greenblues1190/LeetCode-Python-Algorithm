# https://leetcode.com/problems/permutation-in-string/

# Given two strings s1 and s2, return true if s2 contains the permutation of s1.

# In other words, one of s1's permutations is the substring of s2.

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:s1_length - 1])
        for start in range(s2_length - s1_length + 1):
            # s2의 counter를 한칸씩 이동시키며 s1과 비교
            s2_counter[s2[start + s1_length - 1]] += 1
            if s1_counter == s2_counter:
                return True
            s2_counter[s2[start]] -= 1
            if s2_counter[s2[start]] == 0:
                del s2_counter[s2[start]]
        return False