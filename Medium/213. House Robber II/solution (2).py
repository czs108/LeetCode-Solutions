# 213. House Robber II

# Runtime: 24 ms, faster than 94.28% of Python3 online submissions for House Robber II.

# Memory Usage: 14 MB, less than 5.56% of Python3 online submissions for House Robber II.


class Solution:
    # Dynamic Programming
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            # Break the circle
            return max(Solution._robLine(nums[:-1]), # Steal the first.
                        Solution._robLine(nums[1:])) # Steal the last.

    @staticmethod
    def _robLine(nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        count = [0 for _ in range(len(nums) + 1)]
        count[1] = nums[0]
        for i in range(2, len(nums) + 1):
            count[i] = max(count[i - 1], count[i - 2] + nums[i - 1])
        return count[-1]