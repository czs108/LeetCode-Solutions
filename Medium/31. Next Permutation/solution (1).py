# 31. Next Permutation

# Runtime: 44 ms, faster than 60.16% of Python3 online submissions for Next Permutation.

# Memory Usage: 14.4 MB, less than 21.52% of Python3 online submissions for Next Permutation.


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start: int) -> None:
            i, j = start, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        # Create the permutation just larger than the current one.

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]

        reverse(i + 1)