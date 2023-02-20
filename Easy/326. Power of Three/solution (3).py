# 326. Power of Three

# Runtime: 56 ms, faster than 99.49% of Python3 online submissions for Power of Three.

# Memory Usage: 14 MB, less than 98.63% of Python3 online submissions for Power of Three.


from math import log10

class Solution:
    # Mathematics
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            # n = 3^i
            # i = log3(n)
            # i = logx(n) / logx(3)
            # `n` is a power of three if and only if `i` is an integer.
            return (log10(n) / log10(3)) % 1 == 0