# 416. Partition Equal Subset Sum

# Runtime: 1332 ms, faster than 51.16% of Python3 online submissions for Partition Equal Subset Sum.

# Memory Usage: 324.6 MB, less than 5.00% of Python3 online submissions for Partition Equal Subset Sum.


from functools import lru_cache

class Solution:
    # Top Down Dynamic Programming
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        @lru_cache(maxsize=None)
        def dfs(start: int, remain: int) -> bool:
            if remain == 0:
                return True
            elif start == len(nums) - 1 or remain < 0:
                return False
            else:
                return dfs(start + 1, remain) or dfs(start + 1, remain - nums[start])

        return dfs(0, total // 2)