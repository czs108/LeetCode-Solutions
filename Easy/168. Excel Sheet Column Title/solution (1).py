# 168. Excel Sheet Column Title

# Runtime: 28 ms, faster than 73.83% of Python3 online submissions for Excel Sheet Column Title.

# Memory Usage: 13.8 MB, less than 6.25% of Python3 online submissions for Excel Sheet Column Title.


class Solution:
    _BASE = 26
    _ASCII_A = 65

    def convertToTitle(self, n: int) -> str:
        digits = []
        while n != 0:
            digits.append(chr((n - 1) % Solution._BASE + Solution._ASCII_A))
            n = (n - 1) // Solution._BASE
        return "".join(reversed(digits))