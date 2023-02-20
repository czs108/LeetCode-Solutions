# 162. Find Peak Element

# Runtime: 36 ms, faster than 98.26% of Python3 online submissions for Find Peak Element.

# Memory Usage: 14.5 MB, less than 9.77% of Python3 online submissions for Find Peak Element.


class Solution:
    # Linear Scan
    def findPeakElement(self, nums: list[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1