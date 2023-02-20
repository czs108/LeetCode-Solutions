# 1143. Longest Common Subsequence

# Runtime: 2496 ms, faster than 5.01% of Python3 online submissions for Longest Common Subsequence.

# Memory Usage: 24.7 MB, less than 25.08% of Python3 online submissions for Longest Common Subsequence.


class Solution:
    # Dynamic Programming
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lens = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        def lcs(i: int, j: int) -> int:
            if i == 0 or j == 0:
                return 0
            elif lens[i][j] > 0:
                return lens[i][j]

            if text1[i - 1] == text2[j - 1]:
                lens[i][j] = 1 + lcs(i - 1, j - 1)
            else:
                lens[i][j] = max(lcs(i, j - 1), lcs(i - 1, j))
            return lens[i][j]

        return lcs(len(text1), len(text2))