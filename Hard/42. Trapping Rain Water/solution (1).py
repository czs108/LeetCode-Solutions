# 42. Trapping Rain Water

# Time Limit Exceeded


class Solution:
    # Brute Force
    def trap(self, height: list[int]) -> int:
        ans = 0
        for i in range(len(height)):
            left_max, right_max = 0, 0
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
            for j in range(i, len(height)):
                right_max = max(right_max, height[j])
            ans += min(left_max, right_max) - height[i]
        return ans