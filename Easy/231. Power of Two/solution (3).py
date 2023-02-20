# 231. Power of Two

# Runtime: 28 ms, faster than 89.13% of Python3 online submissions for Power of Two.

# Memory Usage: 14.1 MB, less than 67.31% of Python3 online submissions for Power of Two.


class Solution:
    # Turn off the Rightmost 1-bit
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        else:
            return n & (n - 1) == 0