# 326. Power of Three


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            while n % 3 == 0:
                n //= 3
            return n == 1