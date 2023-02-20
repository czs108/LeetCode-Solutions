# 383. Ransom Note

# Runtime: 86 ms, faster than 24.81% of Python3 online submissions for Ransom Note.

# Memory Usage: 14.4 MB, less than 35.80% of Python3 online submissions for Ransom Note.


from collections import Counter

class Solution:
    # Two HashMaps
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        magazine_counts = Counter(magazine)
        ransom_note_counts = Counter(ransomNote)
        for c, n in ransom_note_counts.items():
            if magazine_counts[c] < n:
                return False
        return True