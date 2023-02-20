# 268. Missing Number


class Solution:
    # Sorting
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0

        for i, v in enumerate(nums):
            if i != v:
                return i

        assert False