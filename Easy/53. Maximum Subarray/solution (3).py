# 53. Maximum Subarray

# Runtime: 68 ms, faster than 48.79% of Python3 online submissions for Maximum Subarray.

# Memory Usage: 15.1 MB, less than 12.76% of Python3 online submissions for Maximum Subarray.


class Solution:
    # Dynamic programming
    def maxSubArray(self, nums: list[int]) -> int:
        sums = [0 for _ in nums]
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = max(nums[i], nums[i] + sums[i - 1])
        return max(sums)