# 268. Missing Number

# Runtime: 132 ms, faster than 76.58% of Python3 online submissions for Missing Number.

# Memory Usage: 15.5 MB, less than 51.40% of Python3 online submissions for Missing Number.


class Solution:
    # Gauss' Formula
    def missingNumber(self, nums: list[int]) -> int:
        expected_sum = len(nums) * (len(nums) + 1) // 2
        return expected_sum - sum(nums)