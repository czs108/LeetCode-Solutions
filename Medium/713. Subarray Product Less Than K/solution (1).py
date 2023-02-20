# 713. Subarray Product Less Than K

# Runtime: 688 ms, faster than 91.31% of Python3 online submissions for Subarray Product Less Than K.

# Memory Usage: 17 MB, less than 32.23% of Python3 online submissions for Subarray Product Less Than K.


class Solution:
    # Sliding Window
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        prod = 1
        ans = 0
        left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans