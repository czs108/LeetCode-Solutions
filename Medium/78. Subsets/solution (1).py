# 78. Subsets

# Runtime: 32 ms, faster than 77.06% of Python3 online submissions for Subsets.

# Memory Usage: 14.4 MB, less than 17.60% of Python3 online submissions for Subsets.


class Solution:
    # Backtracking
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return []

        nums.sort()
        res = []

        def backtrack(start: int, subset: list[int]) -> None:
            res.append(list(subset))
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res