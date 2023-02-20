# 198. House Robber

# Runtime: 28 ms, faster than 76.01% of Python3 online submissions for House Robber.

# Memory Usage: 14 MB, less than 9.09% of Python3 online submissions for House Robber.


class Solution:
    # Dynamic Programming
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        count = [0 for _ in range(len(nums) + 1)]
        count[1] = nums[0]
        for i in range(2, len(nums) + 1):
            count[i] = max(count[i - 1], count[i - 2] + nums[i - 1])
        return count[-1]