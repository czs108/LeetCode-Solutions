# 242. Valid Anagram

# Runtime: 103 ms, faster than 5.82% of Python3 online submissions for Valid Anagram.

# Memory Usage: 14.8 MB, less than 29.02% of Python3 online submissions for Valid Anagram.


class Solution:
    # Sorting
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            return sorted(s) == sorted(t)