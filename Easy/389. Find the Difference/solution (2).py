# 389. Find the Difference

# Runtime: 66 ms, faster than 15.47% of Python3 online submissions for Find the Difference.

# Memory Usage: 13.9 MB, less than 87.37% of Python3 online submissions for Find the Difference.


from collections import Counter

class Solution:
    # HashMap
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)

        for c in t:
            if c not in counter_s or counter_s[c] == 0:
                return c
            else:
                counter_s[c] -= 1