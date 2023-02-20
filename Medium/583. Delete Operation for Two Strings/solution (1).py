# 583. Delete Operation for Two Strings

# Runtime: 3352 ms, faster than 5.07% of Python3 online submissions for Delete Operation for Two Strings.

# Memory Usage: 17.6 MB, less than 43.70% of Python3 online submissions for Delete Operation for Two Strings.


class Solution:
    # Longest Common Subsequence
    def minDistance(self, word1: str, word2: str) -> int:
        lens = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        def lcs(i: int, j: int) -> int:
            if i == 0 or j == 0:
                return 0
            elif lens[i][j] > 0:
                return lens[i][j]

            if word1[i - 1] == word2[j - 1]:
                lens[i][j] = 1 + lcs(i - 1, j - 1)
            else:
                lens[i][j] = max(lcs(i, j - 1), lcs(i - 1, j))
            return lens[i][j]

        return len(word1) + len(word2) - 2 * lcs(len(word1), len(word2))