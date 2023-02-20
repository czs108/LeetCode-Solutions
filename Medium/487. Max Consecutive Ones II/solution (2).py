# 487. Max Consecutive Ones II

# Runtime: 420 ms, faster than 12.98% of Python3 online submissions for Max Consecutive Ones II.

# Memory Usage: 14.5 MB, less than 11.06% of Python3 online submissions for Max Consecutive Ones II.


class Solution:
    _FLIP_COUNT = 1

    # Sliding Window
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        assert Solution._FLIP_COUNT > 0

        max_count = 0
        left = 0
        zero_idx = []
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_idx.append(right)
            if len(zero_idx) > Solution._FLIP_COUNT:
                left = zero_idx[0] + 1
                del zero_idx[0]
            max_count = max(max_count, right - left + 1)
        return max_count