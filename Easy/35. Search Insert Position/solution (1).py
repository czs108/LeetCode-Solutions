# 35. Search Insert Position

# Runtime: 44 ms, faster than 91.82% of Python3 online submissions for Search Insert Position.

# Memory Usage: 14.5 MB, less than 5.97% of Python3 online submissions for Search Insert Position.


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] >= target:
                    return i
            return len(nums)