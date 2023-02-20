# 42. Trapping Rain Water

# Runtime: 88 ms, faster than 27.35% of Python3 online submissions for Trapping Rain Water.

# Memory Usage: 15.6 MB, less than 35.74% of Python3 online submissions for Trapping Rain Water.


class Solution:
    # Dynamic Programming
    def trap(self, height: list[int]) -> int:
        ans = 0
        left_highest = [0] * len(height)
        left_highest[0] = height[0]
        for i in range(1, len(height)):
            left_highest[i] = max(height[i], left_highest[i - 1])

        right_highest = [0] * len(height)
        right_highest[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_highest[i] = max(height[i], right_highest[i + 1])

        for i in range(len(height)):
            ans += min(left_highest[i], right_highest[i]) - height[i]
        return ans