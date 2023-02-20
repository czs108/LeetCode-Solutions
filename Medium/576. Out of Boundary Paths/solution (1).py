# 576. Out of Boundary Paths

# Runtime: 259 ms, faster than 30.88% of Python3 online submissions for Out of Boundary Paths.

# Memory Usage: 14.5 MB, less than 91.94% of Python3 online submissions for Out of Boundary Paths.


class Solution:
    # Dynamic Programming
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 1000000007
        ways = [[0] * n for _ in range(m)]
        ways[startRow][startColumn] = 1

        count = 0
        for _ in range(1, maxMove + 1):
            update_ways = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m - 1:
                        count = (count + ways[i][j]) % mod
                    if j == n - 1:
                        count = (count + ways[i][j]) % mod
                    if i == 0:
                        count = (count + ways[i][j]) % mod
                    if j == 0:
                        count = (count + ways[i][j]) % mod

                    if i > 0:
                        update_ways[i][j] += ways[i - 1][j] % mod
                    if j > 0:
                        update_ways[i][j] += ways[i][j - 1] % mod
                    if i < m - 1:
                        update_ways[i][j] += ways[i + 1][j] % mod
                    if j < n - 1:
                        update_ways[i][j] += ways[i][j + 1] % mod
            ways = update_ways
        return count