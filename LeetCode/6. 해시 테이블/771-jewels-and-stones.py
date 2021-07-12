# https://leetcode.com/problems/jewels-and-stones/

# You're given strings jewels representing the types of stones
# that are jewels, and stones representing the stones you have.
# Each character in stones is a type of stone you have.
# You want to know how many of the stones you have are also jewels.

# Letters are case sensitive,
# so "a" is considered a different type of stone from "A".


import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        jewel_count = collections.Counter(stones)

        for jewel in jewels:
            answer += jewel_count[jewel]

        return answer
