# 67. Add Binary

# Runtime: 32 ms, faster than 66.38% of Python3 online submissions for Add Binary.

# Memory Usage: 13.9 MB, less than 5.41% of Python3 online submissions for Add Binary.


class Solution:
    _BASE = 2

    def addBinary(self, a: str, b: str) -> str:
        result = ""
        cf = 0
        i, j = len(a) - 1, len(b) - 1
        while 0 <= i or 0 <= j:
            n = Solution._getDigit(a, i) + Solution._getDigit(b, j) + cf
            cf = n // Solution._BASE
            n %= Solution._BASE
            result = str(n) + result
            i -= 1
            j -= 1

        if cf == 1:
            result = '1' + result
        return result

    @staticmethod
    def _getDigit(s: str, i: int) -> int:
        if 0 <= i and i < len(s):
            return int(s[i])
        else:
            return 0
