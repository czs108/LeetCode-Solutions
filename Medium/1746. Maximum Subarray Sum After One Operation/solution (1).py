# 1746. Maximum Subarray Sum After One Operation

# Runtime: 1356 ms, faster than 36.06% of Python3 online submissions for Maximum Subarray Sum After One Operation.

# Memory Usage: 27.9 MB, less than 88.46% of Python3 online submissions for Maximum Subarray Sum After One Operation.


class Solution:
    # Dynamic Programming
    def maxSumAfterOperation(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]**2 if nums[0]**2 > nums[0] else nums[0]

        NotOp, Op = 0, 1
        sum = [[0] * (len(nums) + 1), [0] * (len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            sum[NotOp][i] = max(sum[NotOp][i - 1] + nums[i - 1], nums[i - 1])
            sum[Op][i] = max(sum[NotOp][i - 1] + nums[i - 1]**2, nums[i - 1]**2, sum[Op][i - 1] + nums[i - 1])
        return max(sum[Op])