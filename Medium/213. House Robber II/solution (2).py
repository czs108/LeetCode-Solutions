# 213. House Robber II

# Runtime: 24 ms, faster than 94.28% of Python3 online submissions for House Robber II.

# Memory Usage: 14 MB, less than 5.56% of Python3 online submissions for House Robber II.


class Solution:
    # Dynamic Programming
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            def rob_line(nums: list[int]) -> int:
                if len(nums) == 0:
                    return 0

                count = [0 for _ in range(len(nums) + 1)]
                count[1] = nums[0]
                for i in range(2, len(nums) + 1):
                    count[i] = max(count[i - 1], count[i - 2] + nums[i - 1])
                return count[-1]

            # Break the circle.
            return max(rob_line(nums[:-1]), # Steal the first.
                        rob_line(nums[1:])) # Steal the last.