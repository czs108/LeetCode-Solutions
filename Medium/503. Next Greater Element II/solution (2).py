# 503. Next Greater Element II

# Runtime: 252 ms, faster than 29.10% of Python3 online submissions for Next Greater Element II.

# Memory Usage: 16 MB, less than 28.65% of Python3 online submissions for Next Greater Element II.


class Solution:
    # Stack
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        res = [-1 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums) * 2 - 1, -1, -1):
            while stack and nums[i % len(nums)] >= stack[-1]:
                stack.pop()
            res[i % len(nums)] = -1 if not stack else stack[-1]
            stack.append(nums[i % len(nums)])
        return res