# 383. Ransom Note

# Runtime: 66 ms, faster than 52.59% of Python3 online submissions for Ransom Note.

# Memory Usage: 14.4 MB, less than 64.42% of Python3 online submissions for Ransom Note.


from collections import Counter

class Solution:
    # Sorting and Stacks
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        magazine_counts = Counter(magazine)
        for c in ransomNote:
            if magazine_counts[c] == 0:
                return False
            else:
                magazine_counts[c] -= 1
        return True