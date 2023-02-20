# 189. Rotate Array

# Runtime: 60 ms, faster than 82.31% of Python3 online submissions for Rotate Array.

# Memory Usage: 15.1 MB, less than 98.36% of Python3 online submissions for Rotate Array.


class Solution:
    # Using Extra Array
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        helper = [0] * len(nums)
        for i in range(len(nums)):
            helper[(i + k) % len(nums)] = nums[i]
        nums[:] = helper