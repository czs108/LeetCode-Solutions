# 152. Maximum Product Subarray

# Runtime: 52 ms, faster than 82.73% of Python3 online submissions for Maximum Product Subarray.

# Memory Usage: 13.8 MB, less than 31.03% of Python3 online submissions for Maximum Product Subarray.


class Solution:
    # Dynamic programming
    def maxProduct(self, nums: List[int]) -> int:
        curr_min_prdct = nums[0]
        curr_max_prdct = nums[0]
        max_prdct = curr_max_prdct
        for i in range(1, len(nums)):
            # `curr_max_prdct` is the max product ending with `nums[i]`.
            # `curr_min_prdct` is the min product ending with `nums[i]`.
            if nums[i] >= 0:
                curr_max_prdct = max(curr_max_prdct * nums[i], nums[i])
                curr_min_prdct = min(curr_min_prdct * nums[i], nums[i])
            else:
                tmp_max_prdct = curr_max_prdct
                curr_max_prdct = max(curr_min_prdct * nums[i], nums[i])
                curr_min_prdct = min(tmp_max_prdct * nums[i], nums[i])
            max_prdct = max(max_prdct, curr_max_prdct)
        return max_prdct