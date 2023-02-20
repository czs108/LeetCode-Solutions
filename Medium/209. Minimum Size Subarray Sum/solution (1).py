# 209. Minimum Size Subarray Sum

# Runtime: 73 ms, faster than 68.51% of Python3 online submissions for Minimum Size Subarray Sum.

# Memory Usage: 16.7 MB, less than 42.21% of Python3 online submissions for Minimum Size Subarray Sum.


class Solution:
    # Two Pointers | Sliding Window
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans = len(nums) + 1
        left = 0
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1
        return ans if ans <= len(nums) else 0