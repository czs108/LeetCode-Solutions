# 2089. Find Target Indices After Sorting Array

# Runtime: 36 ms, faster than 99.17% of Python3 online submissions for Find Target Indices After Sorting Array.

# Memory Usage: 14.3 MB, less than 54.18% of Python3 online submissions for Find Target Indices After Sorting Array.


class Solution:
    # Sort
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        return [i for i, n in enumerate(sorted(nums)) if n == target]