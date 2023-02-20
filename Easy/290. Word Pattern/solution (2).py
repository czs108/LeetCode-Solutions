# 290. Word Pattern

# Runtime: 52 ms, faster than 9.17% of Python3 online submissions for Word Pattern.

# Memory Usage: 14.2 MB, less than 55.03% of Python3 online submissions for Word Pattern.


class Solution:
    # Single Index Hash Map
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        map_index = {}
        for i in range(len(words)):
            c, w = f"char_{pattern[i]}", f"word_{words[i]}"
            if c not in map_index:
                map_index[c] = i
            if w not in map_index:
                map_index[w] = i
            if map_index[c] != map_index[w]:
                return False
        return True