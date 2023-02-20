# 74. Search a 2D Matrix

# Runtime: 44 ms, faster than 66.69% of Python3 online submissions for Search a 2D Matrix.

# Memory Usage: 14.9 MB, less than 32.98% of Python3 online submissions for Search a 2D Matrix.


class Solution:
    # Row Iteration & Binary Search
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        def binary_search(nums: list[int], left: int, right: int) -> bool:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        for i in range(len(matrix)):
            min_val, max_val = matrix[i][0], matrix[i][-1]
            if min_val <= target and target <= max_val:
                return binary_search(matrix[i], 0, len(matrix[0]))
        return False