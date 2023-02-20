# 240. Search a 2D Matrix II

# Runtime: 172 ms, faster than 44.41% of Python3 online submissions for Search a 2D Matrix II.

# Memory Usage: 21 MB, less than 5.67% of Python3 online submissions for Search a 2D Matrix II.


class Solution:
    # Divide and Conquer
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False

        def search_rec(left: int, up: int, right: int, down: int) -> bool:
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right - left) // 2
            # Locate `row` such that matrix[row - 1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                else:
                    row += 1

            return search_rec(left, row, mid - 1, down) or search_rec(mid + 1, up, right, row - 1)

        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)