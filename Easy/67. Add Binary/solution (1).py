# 67. Add Binary

# Runtime: 32 ms, faster than 66.38% of Python3 online submissions for Add Binary.

# Memory Usage: 13.9 MB, less than 5.41% of Python3 online submissions for Add Binary.


class Solution:
    def __init__(self):
        Solution.__base = 2

    def addBinary(self, a: str, b: str) -> str:
        assert 0 < len(a) and len(b) <= 10000
        if len(a) > 1:
            assert a[0] != '0'
        if len(b) > 1:
            assert b[0] != '0'

        result = ""
        cf = 0
        i, j = len(a) - 1, len(b) - 1
        while 0 <= i or 0 <= j:
            n = self.__getDigit(a, i) + self.__getDigit(b, j) + cf
            cf = n // Solution.__base
            n %= Solution.__base
            result = str(n) + result
            i -= 1
            j -= 1

        if cf == 1:
            result = '1' + result
        return result

    def __getDigit(self, s: str, i: int) -> int:
        assert len(s) > 0
        if 0 <= i and i < len(s):
            assert s[i] == '0' or s[i] == '1'
            return int(s[i])
        else:
            return 0
