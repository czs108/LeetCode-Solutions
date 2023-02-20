# 11. Container With Most Water

# Runtime: 862 ms, faster than 27.73% of Python3 online submissions for Container With Most Water.

# Memory Usage: 27.7 MB, less than 22.57% of Python3 online submissions for Container With Most Water.

class Solution:
    # Two Pointers
    def maxArea(self, height: list[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        while left < right:
            low_height = min(height[left], height[right])
            ans = max(ans, low_height * (right - left))
            # The area formed between the lines will always be limited by the height of the shorter line.
            # Further, the farther the lines, the more will be the area obtained.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans