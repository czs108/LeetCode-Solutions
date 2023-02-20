# 2089. Find Target Indices After Sorting Array

# Runtime: 44 ms, faster than 88.20% of Python3 online submissions for Find Target Indices After Sorting Array.

# Memory Usage: 14.2 MB, less than 54.18% of Python3 online submissions for Find Target Indices After Sorting Array.


class Solution:
    # Count
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        equal, smaller = 0, 0
        for n in nums:
            if n < target:
                smaller += 1
            elif n == target:
                equal += 1
        return [i + smaller for i in range(equal)]