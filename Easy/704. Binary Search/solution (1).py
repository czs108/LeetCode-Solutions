# 704. Binary Search

# Runtime: 232 ms, faster than 66.59% of Python3 online submissions for Binary Search.

# Memory Usage: 15.2 MB, less than 41.28% of Python3 online submissions for Binary Search.


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            elif target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1