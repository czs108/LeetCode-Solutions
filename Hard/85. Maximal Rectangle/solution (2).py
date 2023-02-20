# 85. Maximal Rectangle

# Runtime: 204 ms, faster than 74.26% of Python3 online submissions for Maximal Rectangle.

# Memory Usage: 15.3 MB, less than 88.18% of Python3 online submissions for Maximal Rectangle.


class Solution:
    # Histograms - Stack
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        def largest_rectangle_area(heights: list[int]) -> int:
            stack = [-1]
            max_area = 0
            for i in range(len(heights)):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    curr_height = heights[stack.pop()]
                    curr_width = i - stack[-1] - 1
                    max_area = max(max_area, curr_height * curr_width)
                stack.append(i)

            while stack[-1] != -1:
                curr_height = heights[stack.pop()]
                curr_width = len(heights) - stack[-1] - 1
                max_area = max(max_area, curr_height * curr_width)
            return max_area


        max_area = 0
        max_height = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_height[j] = max_height[j] + 1 if matrix[i][j] == "1" else 0
            max_area = max(max_area, largest_rectangle_area(max_height))
        return max_area