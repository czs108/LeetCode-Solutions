# 42. Trapping Rain Water

# Runtime: 131 ms, faster than 12.45% of Python3 online submissions for Trapping Rain Water.

# Memory Usage: 15.7 MB, less than 35.74% of Python3 online submissions for Trapping Rain Water.


class Solution:
    # Using Stacks
    def trap(self, height: list[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop(-1)
                if not stack:
                    break
                # The bar at the top of the stack is bounded by the current bar and a previous bar in the stack.
                dist = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                ans += dist * bounded_height
            stack.append(i)
        return ans