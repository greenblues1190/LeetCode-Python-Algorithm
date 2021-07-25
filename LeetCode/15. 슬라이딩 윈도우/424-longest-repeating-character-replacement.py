# https://leetcode.com/problems/longest-repeating-character-replacement/

# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character.
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter
# you can get after performing the above operations.

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length


import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = collections.defaultdict(int)
        max_freq = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            if right - left + 1 - max_freq > k:
                count[s[left]] -= 1
                left += 1

        return (right + 1) - left
