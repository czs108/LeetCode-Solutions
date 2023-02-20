# 704. Binary Search

# Runtime: 300 ms, faster than 22.77% of Python3 online submissions for Binary Search.

# Memory Usage: 29.8 MB, less than 29.88% of Python3 online submissions for Binary Search.


class Solution:
    def search(self, nums: list[int], target: int) -> int:

        def search_range(left: int, right: int) -> int:
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return search_range(left, mid - 1)
            else:
                return search_range(left + 1, right)

        return search_range(0, len(nums) - 1)