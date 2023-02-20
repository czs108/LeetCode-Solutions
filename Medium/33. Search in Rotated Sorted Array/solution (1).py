# 33. Search in Rotated Sorted Array

# Runtime: 36 ms, faster than 91.45% of Python3 online submissions for Search in Rotated Sorted Array.

# Memory Usage: 14.4 MB, less than 5.87% of Python3 online submissions for Search in Rotated Sorted Array.


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1