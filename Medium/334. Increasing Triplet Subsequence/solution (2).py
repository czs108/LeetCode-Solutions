# 334. Increasing Triplet Subsequence

# Runtime: 885 ms, faster than 15.19% of Python3 online submissions for Increasing Triplet Subsequence.

# Memory Usage: 25.2 MB, less than 49.40% of Python3 online submissions for Increasing Triplet Subsequence.


import math

class Solution:
    # Linear Scan
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        first, second = math.inf, math.inf
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False