# 153. Find Minimum in Rotated Sorted Array

# Runtime: 40 ms, faster than 79.38% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

# Memory Usage: 14.5 MB, less than 59.35% of Python3 online submissions for Find Minimum in Rotated Sorted Array.


class Solution:
    # Binary Search
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1
        if nums[right] > nums[0]:
            return nums[0]

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

        assert False, "No Solution"