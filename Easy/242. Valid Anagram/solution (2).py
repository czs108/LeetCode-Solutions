# 242. Valid Anagram

# Runtime: 28 ms, faster than 99.58% of Python3 online submissions for Valid Anagram.

# Memory Usage: 14.5 MB, less than 82.05% of Python3 online submissions for Valid Anagram.


from collections import Counter

class Solution:
    # Two HashSets
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            return Counter(t) == Counter(s)