# 1991. Find the Middle Index in Array

# Runtime: 43 ms, faster than 40.26% of Python3 online submissions for Find the Middle Index in Array.

# Memory Usage: 13.9 MB, less than 99.63% of Python3 online submissions for Find the Middle Index in Array.


class Solution:
    # Prefix Sum
    def findMiddleIndex(self, nums: list[int]) -> int:
        left_sum, total_sum = 0, sum(nums)
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            else:
                left_sum += nums[i]
        return -1