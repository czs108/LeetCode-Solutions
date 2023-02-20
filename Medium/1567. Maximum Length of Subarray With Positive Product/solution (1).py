# 1567. Maximum Length of Subarray With Positive Product

# Runtime: 640 ms, faster than 65.24% of Python3 online submissions for Maximum Length of Subarray With Positive Product.

# Memory Usage: 28.1 MB, less than 51.12% of Python3 online submissions for Maximum Length of Subarray With Positive Product.


class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        pos_len, neg_len = [0] * len(nums), [0] * len(nums)
        if nums[0] > 0:
            pos_len[0] = 1
        elif nums[0] < 0:
            neg_len[0] = 1

        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos_len[i] = pos_len[i - 1] + 1
                if neg_len[i - 1] != 0:
                    neg_len[i] = neg_len[i - 1] + 1
            elif nums[i] < 0:
                neg_len[i] = pos_len[i - 1] + 1
                if neg_len[i - 1] != 0:
                    pos_len[i] = neg_len[i - 1] + 1
        return max(pos_len)