# 75. Sort Colors

# Runtime: 36 ms, faster than 49.59% of Python3 online submissions for Sort Colors.

# Memory Usage: 14.3 MB, less than 46.53% of Python3 online submissions for Sort Colors.


class Solution:
    # Sorting
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()