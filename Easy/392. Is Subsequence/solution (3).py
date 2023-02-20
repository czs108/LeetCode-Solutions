# 392. Is Subsequence

# Runtime: 28 ms, faster than 90.94% of Python3 online submissions for Is Subsequence.

# Memory Usage: 14.2 MB, less than 74.36% of Python3 online submissions for Is Subsequence.


class Solution:
    # Two Pointers
    def isSubsequence(self, s: str, t: str) -> bool:
        left, right = 0, 0
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
            right += 1
        return left == len(s)