# 162. Find Peak Element

# Runtime: 40 ms, faster than 93.24% of Python3 online submissions for Find Peak Element.

# Memory Usage: 14.3 MB, less than 89.65% of Python3 online submissions for Find Peak Element.


class Solution:
    # Iterative Binary Search
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left