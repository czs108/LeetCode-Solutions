# 747. Largest Number At Least Twice of Others


class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        largest = max(nums)
        largest_idx = nums.index(largest)
        nums.remove(largest)
        second_largest = max(nums)
        if largest >= second_largest * 2:
            return largest_idx
        else:
            return -1