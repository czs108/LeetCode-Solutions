# 448. Find All Numbers Disappeared in an Array

# Runtime: 336 ms, faster than 80.27% of Python3 online submissions for Find All Numbers Disappeared in an Array.

# Memory Usage: 23.7 MB, less than 45.01% of Python3 online submissions for Find All Numbers Disappeared in an Array.


class Solution:
    # Hash Map
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        num_map = {}
        for i in nums:
            num_map[i] = True
        return [i for i in range(1, len(nums) + 1) if i not in num_map]