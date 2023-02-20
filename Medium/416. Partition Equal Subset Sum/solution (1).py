# 416. Partition Equal Subset Sum

# Runtime: 2828 ms, faster than 25.51% of Python3 online submissions for Partition Equal Subset Sum.

# Memory Usage: 29.6 MB, less than 43.08% of Python3 online submissions for Partition Equal Subset Sum.


class Solution:
    # Bottom Up Dynamic Programming
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        half = total // 2

        # `formed[i][j]` is true if the sum `j` can be formed by array elements in subset `nums[0]`...`nums[i]`.
        formed = [[False] * (half + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            formed[i][0] = True

        for i in range(1, len(nums)):
            for j in range(1, half + 1):
                if j - nums[i] < 0:
                    formed[i][j] = formed[i - 1][j]
                else:
                    formed[i][j] = formed[i - 1][j] or formed[i - 1][j - nums[i]]

        return formed[len(nums) - 1][half]