# 485. Max Consecutive Ones

# Runtime: 424 ms, faster than 5.24% of Python3 online submissions for Max Consecutive Ones.

# Memory Usage: 14.3 MB, less than 52.05% of Python3 online submissions for Max Consecutive Ones.


class Solution:
    # Linear Scan
    def __init__(self):
        self._pos = 0
        self._nums = None

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        self._pos = 0
        self._nums = nums
        max_size = 0
        while True:
            size = self._nextWindowSize()
            if size == 0:
                break
            max_size = max(size, max_size)
        return max_size

    def _nextWindowSize(self) -> int:
        while self._pos < len(self._nums) and self._nums[self._pos] != 1:
            self._pos += 1

        size = 0
        while self._pos < len(self._nums) and self._nums[self._pos] != 0:
            size += 1
            self._pos += 1
        return size