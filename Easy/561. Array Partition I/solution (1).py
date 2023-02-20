# 561. Array Partition I

# Runtime: 256 ms, faster than 90.68% of Python3 online submissions for Array Partition I.

# Memory Usage: 16.8 MB, less than 70.31% of Python3 online submissions for Array Partition I.


class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum