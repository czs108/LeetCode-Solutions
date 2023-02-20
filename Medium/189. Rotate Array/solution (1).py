# 189. Rotate Array


class Solution:
    # Brute Force
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            prev = nums[-1]
            for j in range(len(nums)):
                nums[j], prev = prev, nums[j]