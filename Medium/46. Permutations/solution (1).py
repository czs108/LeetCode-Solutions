# 46. Permutations

# Runtime: 68 ms, faster than 9.34% of Python3 online submissions for Permutations.

# Memory Usage: 14.4 MB, less than 42.45% of Python3 online submissions for Permutations.


class Solution:
    # Backtracking
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def backtrack(start: int) -> None:
            if start == len(nums):
                ans.append(nums[:])
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return ans