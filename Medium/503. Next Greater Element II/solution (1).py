# 503. Next Greater Element II

# Runtime: 7036 ms, faster than 5.03% of Python3 online submissions for Next Greater Element II.

# Memory Usage: 15.8 MB, less than 65.18% of Python3 online submissions for Next Greater Element II.


class Solution:
    # Brute Force
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        res = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                val = nums[(i + j) % len(nums)]
                if val > nums[i]:
                    res[i] = val
                    break
        return res