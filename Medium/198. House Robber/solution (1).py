# 198. House Robber

# Runtime: 32 ms, faster than 49.03% of Python3 online submissions for House Robber.

# Memory Usage: 14.1 MB, less than 9.09% of Python3 online submissions for House Robber.


from enum import IntEnum

class Steal(IntEnum):
    No = 0
    Yes = 1


class Solution:
    # Dynamic Programming
    def rob(self, nums: list[int]) -> int:
        count = [[0, 0] for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            count[i][Steal.No] = max(count[i - 1][Steal.No], count[i - 1][Steal.Yes])
            count[i][Steal.Yes] = count[i - 1][Steal.No] + nums[i - 1]
        return max(count[-1][Steal.No], count[-1][Steal.Yes])