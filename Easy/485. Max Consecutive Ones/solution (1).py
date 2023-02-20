# 485. Max Consecutive Ones

# Runtime: 420 ms, faster than 5.19% of Python3 online submissions for Max Consecutive Ones.

# Memory Usage: 14.6 MB, less than 9.41% of Python3 online submissions for Max Consecutive Ones.


class Solution:
    # Linear Scan
    def __init__(self):
        self._pos = 0
        self._nums = None

    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        self._pos = 0
        self._nums = nums
        max_size = 0
        while max_size < len(nums) - self._pos:
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