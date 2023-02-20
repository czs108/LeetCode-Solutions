# 918. Maximum Sum Circular Subarray

# Runtime: 693 ms, faster than 21.43% of Python3 online submissions for Maximum Sum Circular Subarray.

# Memory Usage: 18.5 MB, less than 33.98% of Python3 online submissions for Maximum Sum Circular Subarray.


import math

class Solution:
    # Min & Max
    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        def max_subnums(left: int, right: int) -> int:
            curr_max_sum, max_sum = -math.inf, -math.inf
            for i in range(left, right + 1):
                curr_max_sum = max(nums[i], curr_max_sum + nums[i])
                max_sum = max(max_sum, curr_max_sum)
            return max_sum

        def min_subnums(left: int, right: int) -> int:
            curr_min_sum, min_sum = math.inf, math.inf
            for i in range(left, right + 1):
                curr_min_sum = min(nums[i], curr_min_sum + nums[i])
                min_sum = min(min_sum, curr_min_sum)
            return min_sum

        total = sum(nums)
        ans1 = max_subnums(0, len(nums) - 1)
        ans2 = total - min_subnums(0, len(nums) - 2)
        ans3 = total - min_subnums(1, len(nums) - 1)
        return max(ans1, ans2, ans3)