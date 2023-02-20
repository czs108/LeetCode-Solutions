# 583. Delete Operation for Two Strings

# Runtime: 312 ms, faster than 59.25% of Python3 online submissions for Delete Operation for Two Strings.

# Memory Usage: 18 MB, less than 25.78% of Python3 online submissions for Delete Operation for Two Strings.


class Solution:
    # Dynamic Programmming
    def minDistance(self, word1: str, word2: str) -> int:
        counts = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    counts[i][j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    counts[i][j] = counts[i - 1][j - 1]
                else:
                    counts[i][j] = 1 + min(counts[i - 1][j], counts[i][j - 1])
        return counts[-1][-1]