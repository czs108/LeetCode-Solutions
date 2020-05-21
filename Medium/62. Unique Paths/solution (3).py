# 62. Unique Paths

# Runtime: 24 ms, faster than 93.52% of Python3 online submissions for Unique Paths.

# Memory Usage: 13.9 MB, less than 5.77% of Python3 online submissions for Unique Paths.


class Solution:
    # Dynamic programming - Bottom up
    def uniquePaths(self, m: int, n: int) -> int:
        # Rolling array
        prev, curr = 0, 0
        count = [[0 for _ in range(n)] for _ in range(2)]
        for i in range(m):
            # Roll
            prev = curr
            curr = 1 - curr
            for j in range(n):
                if i == 0 or j == 0:
                    count[curr][j] = 1
                else:
                    count[curr][j] = count[prev][j] + count[curr][j - 1]
        return count[curr][-1]
