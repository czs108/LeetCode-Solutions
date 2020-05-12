# 62. Unique Paths

# Runtime: 32 ms, faster than 49.86% of Python3 online submissions for Unique Paths.

# Memory Usage: 13.9 MB, less than 5.77% of Python3 online submissions for Unique Paths.


class Solution:
    # Dynamic programming - Top down
    def __init__(self):
        self.__count = None

    def uniquePaths(self, m: int, n: int) -> int:
        self.__count = [[0 for _ in range(n)] for _ in range(m)]
        return self.__uniquePaths(m - 1, n - 1)

    def __uniquePaths(self, i: int, j: int) -> int:
        if i < 0 or j < 0:
            return 0
        elif i == 0 or j == 0:
            return 1
        elif self.__count[i][j] != 0:
            return self.__count[i][j]

        self.__count[i][j] = self.__uniquePaths(i - 1, j) + self.__uniquePaths(i, j - 1)
        return self.__count[i][j]
    