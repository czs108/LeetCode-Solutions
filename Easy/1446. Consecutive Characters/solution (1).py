# 1446. Consecutive Characters

# Runtime: 48 ms, faster than 44.19% of Python3 online submissions for Consecutive Characters.

# Memory Usage: 14.2 MB, less than 45.10% of Python3 online submissions for Consecutive Characters.


class Solution:
    # One Pass
    def maxPower(self, s: str) -> int:
        max_count, count = 0, 0
        prev = None
        for c in s:
            if c == prev:
                count += 1
            else:
                prev = c
                count = 1
            max_count= max(max_count, count)
        return max_count