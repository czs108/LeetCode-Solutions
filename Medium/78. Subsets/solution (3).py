# 78. Subsets

# Runtime: 20 ms, faster than 99.87% of Python3 online submissions for Subsets.

# Memory Usage: 14.3 MB, less than 92.80% of Python3 online submissions for Subsets.


class Solution:
    # Backtracking
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return []

        nums.sort()
        res = []

        def backtrack(start: int, subset: list[int]) -> None:
            if start == len(nums):
                res.append(list(subset))
            else:
                # Do not contain the current number.
                backtrack(start + 1, subset)

                # Contain the current number.
                subset.append(nums[start])
                backtrack(start + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res