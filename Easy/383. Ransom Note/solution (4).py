# 383. Ransom Note

# Runtime: 160 ms, faster than 5.37% of Python3 online submissions for Ransom Note.

# Memory Usage: 14.6 MB, less than 11.24% of Python3 online submissions for Ransom Note.


class Solution:
    # Sorting and Stacks
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        ransomNote = sorted(ransomNote, reverse=True)
        magazine = sorted(magazine, reverse=True)
        while len(ransomNote) > 0 and len(magazine) > 0:
            if ransomNote[-1] == magazine[-1]:
                ransomNote.pop()
                magazine.pop()
            elif ransomNote[-1] > magazine[-1]:
                magazine.pop()
            else:
                return False
        return len(ransomNote) == 0