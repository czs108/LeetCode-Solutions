# 383. Ransom Note

# Runtime: 28 ms, faster than 99.31% of Python3 online submissions for Ransom Note.

# Memory Usage: 14.2 MB, less than 85.49% of Python3 online submissions for Ransom Note.


class Solution:
    # Simulation
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for c in ransomNote:
            if c not in magazine:
                return False
            else:
                idx = magazine.index(c)
                magazine = magazine[:idx] + magazine[idx + 1:]
        return True