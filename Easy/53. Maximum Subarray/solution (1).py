# 53. Maximum Subarray

# Runtime: 116 ms, faster than 8.83% of Python3 online submissions for Maximum Subarray.

# Memory Usage: 14.4 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.


class Solution:
    # Dynamic programming
    def maxSubArray(self, nums: list[int]) -> int:
        curr_max_sum = nums[0]
        max_sum = curr_max_sum
        for i in range(1, len(nums)):
            # `curr_max_sum` is the max sum ending with `nums[i]`.
            curr_max_sum = max(curr_max_sum + nums[i], nums[i])
            max_sum = max(curr_max_sum, max_sum)
        return max_sum