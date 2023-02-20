# 152. Maximum Product Subarray

# Runtime: 52 ms, faster than 86.10% of Python3 online submissions for Maximum Product Subarray.

# Memory Usage: 14.4 MB, less than 36.06% of Python3 online submissions for Maximum Product Subarray.


class Solution:
    # Dynamic programming
    def maxProduct(self, nums: list[int]) -> int:
        curr_min_prdct = nums[0]
        curr_max_prdct = nums[0]
        max_prdct = curr_max_prdct
        for i in range(1, len(nums)):
            prev_min_prdct, prev_max_prdct = curr_min_prdct, curr_max_prdct
            curr_min_prdct = min(nums[i], prev_min_prdct * nums[i], prev_max_prdct * nums[i])
            curr_max_prdct = max(nums[i], prev_min_prdct * nums[i], prev_max_prdct * nums[i])
            max_prdct = max(max_prdct, curr_max_prdct)
        return max_prdct