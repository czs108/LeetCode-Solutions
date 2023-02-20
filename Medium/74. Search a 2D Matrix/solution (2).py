# 74. Search a 2D Matrix

# Runtime: 44 ms, faster than 66.69% of Python3 online submissions for Search a 2D Matrix.

# Memory Usage: 14.7 MB, less than 86.28% of Python3 online submissions for Search a 2D Matrix.


class Solution:
    # Binary Search
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        height, width = len(matrix), len(matrix[0])

        def matrix_val(idx: int) -> int:
            return matrix[idx // width][idx % width]

        left, right = 0, height * width - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = matrix_val(mid)
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False