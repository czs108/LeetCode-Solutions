# 1015. Smallest Integer Divisible by K

# Runtime: 52 ms, faster than 67.57% of Python3 online submissions for Smallest Integer Divisible by K.

# Memory Usage: 14.2 MB, less than 86.49% of Python3 online submissions for Smallest Integer Divisible by K.


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        for i in range(1, k + 1):
            # n = n * 10 + 1
            # remainder = n % k
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return i
        return -1