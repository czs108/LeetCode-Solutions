# 172. Factorial Trailing Zeroes

# Runtime: 28 ms, faster than 76.98% of Python3 online submissions for Factorial Trailing Zeroes.

# Memory Usage: 13.9 MB, less than 10.00% of Python3 online submissions for Factorial Trailing Zeroes.


class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Each 0 on the end of the factorial represents a multiplication by 10.
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count