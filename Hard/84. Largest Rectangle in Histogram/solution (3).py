# 84. Largest Rectangle in Histogram

# Runtime: 764 ms, faster than 90.44% of Python3 online submissions for Largest Rectangle in Histogram.

# Memory Usage: 26.8 MB, less than 99.49% of Python3 online submissions for Largest Rectangle in Histogram.


class Solution:
    # Stack
    def largestRectangleArea(self, heights: list[int]) -> int:
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