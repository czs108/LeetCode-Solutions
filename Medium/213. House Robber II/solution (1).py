# 213. House Robber II

# Runtime: 32 ms, faster than 55.39% of Python3 online submissions for House Robber II.

# Memory Usage: 13.9 MB, less than 5.56% of Python3 online submissions for House Robber II.


from enum import IntEnum

class Steal(IntEnum):
    No = 0
    Yes = 1


class Solution:
    # Dynamic Programming
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            def rob_line(nums: list[int]) -> int:
                count = [[0, 0] for _ in range(len(nums) + 1)]
                for i in range(1, len(nums) + 1):
                    count[i][Steal.No] = max(count[i - 1][Steal.No], count[i - 1][Steal.Yes])
                    count[i][Steal.Yes] = count[i - 1][Steal.No] + nums[i - 1]
                return max(count[-1][Steal.No], count[-1][Steal.Yes])

            # Break the circle.
            return max(rob_line(nums[:-1]), # Steal the first.
                        rob_line(nums[1:])) # Steal the last.