# 290. Word Pattern

# Runtime: 37 ms, faster than 26.65% of Python3 online submissions for Word Pattern.

# Memory Usage: 14.1 MB, less than 80.62% of Python3 online submissions for Word Pattern.


class Solution:
    # Two Hash Maps
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        map_char, map_word = {}, {}
        for c, w in zip(pattern, words):
            if c not in map_char:
                if w in map_word:
                    return False
                else:
                    map_char[c] = w
                    map_word[w] = c
            else:
                if map_char[c] != w:
                    return False
        return True