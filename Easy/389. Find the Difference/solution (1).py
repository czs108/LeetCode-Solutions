# 389. Find the Difference

# Runtime: 73 ms, faster than 9.38% of Python3 online submissions for Find the Difference.

# Memory Usage: 13.9 MB, less than 96.75% of Python3 online submissions for Find the Difference.


class Solution:
    # Sorting
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        i = 0
        while i < len(sorted_s):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]
            else:
                i += 1
        return sorted_t[i]