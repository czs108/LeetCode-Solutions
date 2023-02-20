# 674. Longest Continuous Increasing Subsequence

# Runtime: 200 ms, faster than 5.36% of Python3 online submissions for Longest Continuous Increasing Subsequence.

# Memory Usage: 15 MB, less than 8.70% of Python3 online submissions for Longest Continuous Increasing Subsequence.


class Solution:
    # Sliding Window
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i - 1] >= nums[i]:
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans