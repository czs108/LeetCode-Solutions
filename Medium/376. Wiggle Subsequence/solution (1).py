# 376. Wiggle Subsequence

# Runtime: 184 ms, faster than 19.17% of Python3 online submissions for Wiggle Subsequence.

# Memory Usage: 14.4 MB, less than 38.25% of Python3 online submissions for Wiggle Subsequence.


class Solution:
    # Dynamic Programming
    def wiggleMaxLength(self, nums: list[int]) -> int:
        pos, neg = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            neg[i], pos[i] = neg[i - 1], pos[i - 1]
            for j in range(i):
                if nums[i] > nums[j]:
                    pos[i] = max(pos[i], neg[j] + 1)
                elif nums[i] < nums[j]:
                    neg[i] = max(neg[i], pos[j] + 1)
        return max(max(pos), max(neg))