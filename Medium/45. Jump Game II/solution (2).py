# 45. Jump Game II

# Runtime: 7142 ms, faster than 20.83% of Python3 online submissions for Jump Game II.

# Memory Usage: 15.2 MB, less than 48.82% of Python3 online submissions for Jump Game II.


import math

class Solution:
    # Dynamic Programming
    def jump(self, nums: list[int]) -> int:
        jmps = [math.inf for _ in range(len(nums))]
        jmps[0] = 0
        for i in range(len(nums) - 1):
            farthest = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, farthest + 1):
                jmps[j] = min(jmps[j], jmps[i] + 1)
        return jmps[-1]