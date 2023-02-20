# 59. Spiral Matrix II

# Runtime: 42 ms, faster than 24.22% of Python3 online submissions for Spiral Matrix II.

# Memory Usage: 14.4 MB, less than 51.12% of Python3 online submissions for Spiral Matrix II.


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        mat = [[0] * n for _ in range(n)]
        i = 1
        up, down = 0, n - 1
        left, right = 0, n - 1
        while i <= n**2:
            # Traverse from left to right.
            for col in range(left, right + 1):
                mat[up][col] = i
                i += 1

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                mat[row][right] = i
                i += 1

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    mat[down][col] = i
                    i += 1

            # Make sure we are now on a different column.
            if left != right:
                for row in range(down - 1, up, -1):
                    mat[row][left] = i
                    i += 1

            left += 1
            right -= 1
            up += 1
            down -= 1

        return mat