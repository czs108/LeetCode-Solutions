# 326. Power of Three

# Runtime: 108 ms, faster than 39.33% of Python3 online submissions for Power of Three.

# Memory Usage: 14.3 MB, less than 15.34% of Python3 online submissions for Power of Three.


class Solution:
    # Base Conversion
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            digits = []
            # If we convert the number to base 3 and the representation is of the form 100...0,
            # then the number is a power of 3.
            while n:
                digits.append(int(n % 3))
                n //= 3
            return sum(digits) == 1