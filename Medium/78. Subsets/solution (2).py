# 78. Subsets

# Runtime: 32 ms, faster than 85.43% of Python3 online submissions for Subsets.

# Memory Usage: 14.3 MB, less than 78.59% of Python3 online submissions for Subsets.


class Solution:
    # Cascading
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        for n in nums:
            res += [curr + [n] for curr in res]
        return res