# 739. Daily Temperatures

# Runtime: 1328 ms, faster than 20.52% of Python3 online submissions for Daily Temperatures.

# Memory Usage: 33.7 MB, less than 5.15% of Python3 online submissions for Daily Temperatures.


class Solution:
    # Stack
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        idx = {}
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx[stack.pop()] = i
            stack.append(i)

        while stack:
            idx[stack.pop()] = -1

        return [idx[i] - i if idx[i] != -1 else 0 for i in range(len(temperatures))]