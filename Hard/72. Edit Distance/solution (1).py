# 72. Edit Distance

# Runtime: 216 ms, faster than 29.11% of Python3 online submissions for Edit Distance.

# Memory Usage: 17.6 MB, less than 15.38% of Python3 online submissions for Edit Distance.


class Solution:
    # Dynamic programming
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        if len1 == 0:
            return len2
        elif len2 == 0:
            return len1

        # Set up initial costs on horizontal and vertical.
        dist = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        for i in range(1, len1 + 1):
            dist[i][0] = i
        for j in range(1, len2 + 1):
            dist[0][j] = j

        # Compute the best.
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # Convert `word1` to `word2`.
                replace = dist[i - 1][j - 1] + (1 if word1[i - 1] != word2[j - 1] else 0)
                remove = dist[i - 1][j] + 1
                insert = dist[i][j - 1] + 1
                dist[i][j] = min(replace, remove, insert)
        return dist[len1][len2]