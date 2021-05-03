# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_length = len(s)
        p_length = len(p)
        ans = []
        p_Counter = Counter(p)
        s_Counter = Counter(s[:p_length-1])  # s[0:len(p)-1] 까지 미리 카운트

        for i in range(0, s_length - p_length + 1):
            s_Counter[s[i + p_length - 1]] += 1   # 새로운 문자 카운트
            if s_Counter == p_Counter:
                # Counter(s)와 Counter(p)가 같으면 anagram이므로 시작 index 저장
                ans.append(i)
            s_Counter[s[i]] -= 1    # 가장 오래된 문자의 카운트 감소
            if s_Counter[s[i]] == 0:
                # 만약 그 문자의 카운트가 0이라면 제거
                del s_Counter[s[i]]

        return ans