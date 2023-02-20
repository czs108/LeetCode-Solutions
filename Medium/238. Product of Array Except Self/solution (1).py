# 238. Product of Array Except Self

# Runtime: 318 ms, faster than 22.10% of Python3 online submissions for Product of Array Except Self.

# Memory Usage: 22.4 MB, less than 15.83% of Python3 online submissions for Product of Array Except Self.


class Solution:
    # Dynamic Programming | Left and Right Products
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_prdct = [0] * len(nums)
        left_prdct[0] = 1
        for i in range(1, len(nums)):
            left_prdct[i] = left_prdct[i - 1] * nums[i - 1]
            if left_prdct[i] == 0:
                break

        right_prdct = [0] * len(nums)
        right_prdct[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            right_prdct[i] = right_prdct[i + 1] * nums[i + 1]
            if right_prdct[i] == 0:
                break

        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = left_prdct[i] * right_prdct[i]
        return ans