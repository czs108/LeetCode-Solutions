# 84. Largest Rectangle in Histogram

# Time Limit Exceeded


class Solution:
    # Divide & Conquer
    #
    # The rectangle with maximum area will be the maximum of:
    # The widest possible rectangle with height equal to the height of the shortest bar.
    # The largest rectangle confined to the left of the shortest bar (subproblem).
    # The largest rectangle confined to the right of the shortest bar (subproblem).
    def largestRectangleArea(self, heights: list[int]) -> int:

        def calc_area(start: int, end: int) -> int:
            if start > end:
                return 0
            min_idx = start
            for i in range(start, end + 1):
                if heights[i] < heights[min_idx]:
                    min_idx = i
            return max(heights[min_idx] * (end - start + 1),
                        calc_area(start, min_idx - 1),
                        calc_area(min_idx + 1, end))

        return calc_area(0, len(heights) - 1)