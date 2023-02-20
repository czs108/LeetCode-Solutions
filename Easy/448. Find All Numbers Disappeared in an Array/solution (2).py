# 448. Find All Numbers Disappeared in an Array

# Runtime: 380 ms, faster than 40.61% of Python3 online submissions for Find All Numbers Disappeared in an Array.

# Memory Usage: 21.7 MB, less than 92.11% of Python3 online submissions for Find All Numbers Disappeared in an Array.


class Solution:
    # O(1) Space InPlace Modification Solution
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            val = abs(nums[i])
            if nums[val - 1] > 0:
                nums[val - 1] = -nums[val - 1]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]