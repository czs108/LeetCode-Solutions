# 231. Power of Two

# Runtime: 32 ms, faster than 71.67% of Python3 online submissions for Power of Two.

# Memory Usage: 14.2 MB, less than 67.31% of Python3 online submissions for Power of Two.


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        else:
            while n % 2 == 0:
                n /= 2
            return n == 1