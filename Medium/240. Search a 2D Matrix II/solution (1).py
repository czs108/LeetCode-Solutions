# 240. Search a 2D Matrix II

# Runtime: 36 ms, faster than 63.02% of Python3 online submissions for Search a 2D Matrix II.

# Memory Usage: 18.7 MB, less than 70.91% of Python3 online submissions for Search a 2D Matrix II.


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        elif target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        # Search from right-top to left-bottom.
        x, y = 0, len(matrix[0]) - 1
        while x < len(matrix) and y >= 0:
            if matrix[x][y] < target:
                x += 1
            elif matrix[x][y] > target:
                y -= 1
            else:
                return True
        return False