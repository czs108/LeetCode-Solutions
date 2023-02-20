# 189. Rotate Array

# Runtime: 60 ms, faster than 82.31% of Python3 online submissions for Rotate Array.

# Memory Usage: 15.3 MB, less than 64.16% of Python3 online submissions for Rotate Array.


# Using Reverse

# Let n = 7 and k = 3
# Original List                   : 1 2 3 4 5 6 7
# After reversing all numbers     : 7 6 5 4 3 2 1
# After reversing first k numbers : 5 6 7 4 3 2 1
# After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        k %= len(nums)
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)