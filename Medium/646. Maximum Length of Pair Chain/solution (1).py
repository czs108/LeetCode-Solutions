# 646. Maximum Length of Pair Chain

# Runtime: 329 ms, faster than 48.42% of Python3 online submissions for Maximum Length of Pair Chain.

# Memory Usage: 14.8 MB, less than 60.45% of Python3 online submissions for Maximum Length of Pair Chain.


import math

class Solution:
    # Greedy
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        curr_y = -math.inf
        count = 0
        pairs.sort(key=lambda p: p[1])
        for x, y in pairs:
            if curr_y < x:
                curr_y = y
                count += 1
        return count