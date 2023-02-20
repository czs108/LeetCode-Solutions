# 29. Divide Two Integers


class Solution:
    _MAX_INT = 2**31 - 1
    _MIN_INT = -2**31

    # Repeated Subtraction
    def divide(self, dividend: int, divisor: int) -> int:
        # Special case: overflow.
        if dividend == self._MIN_INT and divisor == -1:
            return self._MAX_INT

        # Convert both numbers to negatives.
        # Because there are more negative signed 32-bit integers than there are positive signed 32-bit integers.
        # Each positive signed 32-bit integer has a corresponding negative signed 32-bit integer.
        # However, the same is not true for negative signed 32-bit integers.
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0
        while dividend - divisor <= 0:
            dividend -= divisor
            quotient -= 1
        return -quotient if negatives != 1 else quotient