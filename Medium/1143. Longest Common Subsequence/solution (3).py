# 1143. Longest Common Subsequence

# Runtime: 416 ms, faster than 69.20% of Python3 online submissions for Longest Common Subsequence.

# Memory Usage: 22.8 MB, less than 40.40% of Python3 online submissions for Longest Common Subsequence.


class Solution:
    # Dynamic Programming
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0

        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]