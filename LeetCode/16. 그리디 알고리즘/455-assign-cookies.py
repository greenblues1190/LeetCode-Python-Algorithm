# https://leetcode.com/problems/assign-cookies/

# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie\
# that the child will be content with; and each cookie j has a size s[j].
# If s[j] >= g[i], we can assign the cookie j to the child i, and the child i
# will be content. Your goal is to maximize the number of your content children
# and output the maximum number.

# Constraints:

# 1 <= g.length <= 3 * 104
# 0 <= s.length <= 3 * 104
# 1 <= g[i], s[j] <= 231 - 1


from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        greed_idx = size_idx = 0

        while greed_idx < len(g) and size_idx < len(s):
            if g[greed_idx] <= s[size_idx]:
                greed_idx += 1
            size_idx += 1

        return greed_idx
