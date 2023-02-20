# 42. Trapping Rain Water

# Runtime: 99 ms, faster than 21.40% of Python3 online submissions for Trapping Rain Water.

# Memory Usage: 15.7 MB, less than 35.74% of Python3 online submissions for Trapping Rain Water.


class Solution:
    # Two Pointers
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans