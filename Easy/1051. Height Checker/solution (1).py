# 1051. Height Checker


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        count = 0
        sort_heights = sorted(heights)
        for i, j in zip(sort_heights, heights):
            if i != j:
                count += 1
        return count