# 136. Single Number


class Solution:
    # Math
    def singleNumber(self, nums: List[int]) -> int:
        # 2 ∗ (a + b + c) − (a + a + b + b + c) = c
        return 2 * sum(set(nums)) - sum(nums)