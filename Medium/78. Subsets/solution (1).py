# 78. Subsets

# Runtime: 32 ms, faster than 77.06% of Python3 online submissions for Subsets.

# Memory Usage: 14.4 MB, less than 17.60% of Python3 online submissions for Subsets.


class Solution:
    def __init__(self):
        self._subsets = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        nums.sort()
        self._helper(nums, 0, [])
        return self._subsets

    def _helper(self, nums: List[int], begin: int, subset: List[int]):
        self._subsets.append(list(subset))

        for i in range(begin, len(nums)):
            # Do a choice
            subset.append(nums[i])
            # Backtrack
            self._helper(nums, i + 1, subset)
            # Undo the choice
            del subset[-1]