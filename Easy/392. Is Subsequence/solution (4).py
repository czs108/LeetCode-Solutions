# 392. Is Subsequence

# Runtime: 104 ms, faster than 6.10% of Python3 online submissions for Is Subsequence.

# Memory Usage: 15 MB, less than 9.86% of Python3 online submissions for Is Subsequence.


class Solution:
    # Dynamic Programming | Edit Distance
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        elif len(s) == len(t):
            return s == t

        # Matrix to store the history of matches/deletions.
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for j in range(1, len(t) + 1):
            for i in range(1, len(s) + 1):
                if s[i - 1] == t[j - 1]:
                    # Find another match.
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Retrieve the maximal result from previous prefixes.
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

            # Check if we can consume the entire source string with the current prefix of the target string.
            if dp[len(s)][j] == len(s):
                return True

        return False