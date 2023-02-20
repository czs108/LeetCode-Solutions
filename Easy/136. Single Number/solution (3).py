# 136. Single Number

# Runtime: 88 ms, faster than 64.02% of Python3 online submissions for Single Number.

# Memory Usage: 16.5 MB, less than 6.56% of Python3 online submissions for Single Number.


class Solution:
    # Bit Manipulation
    def singleNumber(self, nums: list[int]) -> int:
        n = 0
        for i in nums:
            n ^= i
        return n