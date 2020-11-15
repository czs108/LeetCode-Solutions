# 90. Subsets II

# Runtime: 40 ms, faster than 45.48% of Python3 online submissions for Subsets II.

# Memory Usage: 14.3 MB, less than 23.87% of Python3 online submissions for Subsets II.


class Solution:
    def __init__(self):
        self._subsets = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        nums.sort()
        self._helper(nums, 0, [])
        return self._subsets

    def _helper(self, nums: List[int], begin: int, subset: List[int]):
        self._subsets.append(list(subset))

        for i in range(begin, len(nums)):
            # The same value has been added.
            if i != 0 and nums[i] == nums[i - 1] and i > begin:
                continue
            # Do a choice
            subset.append(nums[i])
            # Backtrack
            self._helper(nums, i + 1, subset)
            # Undo the choice
            del subset[-1]