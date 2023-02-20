# 739. Daily Temperatures

# Runtime: 1232 ms, faster than 61.26% of Python3 online submissions for Daily Temperatures.

# Memory Usage: 25.4 MB, less than 62.05% of Python3 online submissions for Daily Temperatures.


class Solution:
    # Stack
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            res[i] = 0 if not stack else stack[-1] - i
            stack.append(i)
        return res