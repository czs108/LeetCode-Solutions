# 371. Sum of Two Integers


class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)

        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # Sum of two positive integers x + y.
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            # Difference of two positive integers x - y.
            while y:
                x, y = x ^ y, ((~x) & y) << 1

        return x * sign