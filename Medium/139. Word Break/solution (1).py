# 139. Word Break

# Runtime: 40 ms, faster than 65.96% of Python3 online submissions for Word Break.

# Memory Usage: 14.5 MB, less than 45.76% of Python3 online submissions for Word Break.


from functools import lru_cache

class Solution:
    # Recursion with Memoization
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = frozenset(wordDict)

        @lru_cache
        def word_break_memo(start: int) -> bool:
            if start == len(s):
                return True
            else:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in words and word_break_memo(end):
                        return True
                return False

        return word_break_memo(0)