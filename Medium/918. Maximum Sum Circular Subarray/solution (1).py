# 918. Maximum Sum Circular Subarray

# Runtime: 1028 ms, faster than 5.09% of Python3 online submissions for Maximum Sum Circular Subarray.

# Memory Usage: 18.6 MB, less than 33.98% of Python3 online submissions for Maximum Sum Circular Subarray.


import math

class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        def max_one_interval() -> int:
            curr_max_sum, max_sum = -math.inf, -math.inf
            for x in nums:
                curr_max_sum = max(x, curr_max_sum + x)
                max_sum = max(max_sum, curr_max_sum)
            return max_sum

        def max_two_interval() -> int:
            right_sums = [-math.inf] * len(nums)
            right_sums[-1] = nums[-1]
            for i in range(len(nums) - 2, -1, -1):
                right_sums[i] = right_sums[i + 1] + nums[i]

            max_right_sums = [-math.inf] * len(nums)
            max_right_sums[-1] = right_sums[-1]
            for i in range(len(nums) - 2, -1, -1):
                max_right_sums[i] = max(max_right_sums[i + 1], right_sums[i])

            max_sum = -math.inf
            left_sum = 0
            for i in range(len(nums) - 2):
                left_sum += nums[i]
                max_sum = max(max_sum, left_sum + max_right_sums[i + 2])
            return max_sum

        return max(max_one_interval(), max_two_interval())