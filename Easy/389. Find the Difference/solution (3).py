# 389. Find the Difference

# Runtime: 56 ms, faster than 30.73% of Python3 online submissions for Find the Difference.

# Memory Usage: 13.9 MB, less than 96.75% of Python3 online submissions for Find the Difference.


class Solution:
    # Bit Manipulation
    def findTheDifference(self, s: str, t: str) -> str:
        remain = 0

        for c in s:
            remain ^= ord(c)

        for c in t:
            remain ^= ord(c)

        return chr(remain)