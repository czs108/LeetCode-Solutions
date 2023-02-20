# 54. Spiral Matrix


class Solution:
    # Set Up Boundaries
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row, col = len(matrix), len(matrix[0])
        res = []
        up = left = 0
        right = col - 1
        down = row - 1
        while len(res) < row * col:
            # Traverse from left to right.
            for col in range(left, right + 1):
                res.append(matrix[up][col])

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                res.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    res.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1
        return res