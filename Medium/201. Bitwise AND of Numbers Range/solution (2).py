# 201. Bitwise AND of Numbers Range

# Runtime: 44 ms, faster than 98.60% of Python3 online submissions for Bitwise AND of Numbers Range.

# Memory Usage: 14.3 MB, less than 58.10% of Python3 online submissions for Bitwise AND of Numbers Range.


class Solution:
    # Brian Kernighan's algorithm
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return left & right