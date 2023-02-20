# 242. Valid Anagram

# Runtime: 28 ms, faster than 61.58% of Python3 online submissions for Valid Anagram.

# Memory Usage: 14.5 MB, less than 95.05% of Python3 online submissions for Valid Anagram.


from collections import Counter

class Solution:
    # One HashSet
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            count = Counter(t)
            for c in s:
                count[c] -= 1

            for n in count.values():
                if n != 0:
                    return False
            return True