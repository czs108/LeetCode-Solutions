# 201. Bitwise AND of Numbers Range

# Runtime: 60 ms, faster than 65.36% of Python3 online submissions for Bitwise AND of Numbers Range.

# Memory Usage: 14.2 MB, less than 58.10% of Python3 online submissions for Bitwise AND of Numbers Range.


class Solution:
    # Bit Shift | Common Prefix
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left != right:
            right >>= 1
            left >>= 1
            shift += 1
        return left << shift