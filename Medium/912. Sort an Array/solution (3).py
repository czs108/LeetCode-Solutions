# 912. Sort an Array

# Time Limit Exceeded


class Solution:
    # Insertion Sort
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums