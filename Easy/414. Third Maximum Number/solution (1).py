# 414. Third Maximum Number


class Solution:
    # Use a Set and Delete Maximums
    def thirdMax(self, nums: list[int]) -> int:
        # Make a Set with the input.
        nums = set(nums)

        # Find the maximum.
        max_num = max(nums)

        # Check whether or not this is a case where
        # we need to return the maximum.
        if len(nums) < 3:
            return max_num

        # Otherwise, continue on to finding the third maximum.
        nums.remove(max_num)
        second_max_num = max(nums)
        nums.remove(second_max_num)
        return max(nums)