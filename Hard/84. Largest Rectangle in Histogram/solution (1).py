# 84. Largest Rectangle in Histogram

# Time Limit Exceeded


import math

class Solution:
    # Brute Force
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            min_height = math.inf
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area