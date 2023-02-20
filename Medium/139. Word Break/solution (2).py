# 139. Word Break

# Runtime: 36 ms, faster than 84.11% of Python3 online submissions for Word Break.

# Memory Usage: 14.5 MB, less than 24.97% of Python3 online submissions for Word Break.


class Solution:
    # Dynamic Programming
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = frozenset(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]