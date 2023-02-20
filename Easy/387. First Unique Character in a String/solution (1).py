# 387. First Unique Character in a String

# Runtime: 100 ms, faster than 76.54% of Python3 online submissions for First Unique Character in a String.

# Memory Usage: 14.5 MB, less than 43.92% of Python3 online submissions for First Unique Character in a String.


from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1