# 376. Wiggle Subsequence

# Runtime: 28 ms, faster than 96.04% of Python3 online submissions for Wiggle Subsequence.

# Memory Usage: 14.4 MB, less than 12.90% of Python3 online submissions for Wiggle Subsequence.


class Solution:
    # Linear Dynamic Programming
    def wiggleMaxLength(self, nums: list[int]) -> int:
        pos, neg = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                pos[i] = neg[i - 1] + 1
                neg[i] = neg[i - 1]
            elif nums[i] < nums[i - 1]:
                pos[i] = pos[i - 1]
                neg[i] = pos[i - 1] + 1
            else:
                pos[i] = pos[i - 1]
                neg[i] = neg[i - 1]
        return max(max(pos), max(neg))