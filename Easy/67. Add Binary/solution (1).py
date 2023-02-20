# 67. Add Binary

# Runtime: 32 ms, faster than 66.38% of Python3 online submissions for Add Binary.

# Memory Usage: 13.9 MB, less than 5.41% of Python3 online submissions for Add Binary.


class Solution:
    _BASE = 2

    def addBinary(self, a: str, b: str) -> str:

        def get_digit(s: str, i: int) -> int:
            if 0 <= i and i < len(s):
                return int(s[i])
            else:
                return 0

        ans = ""
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while 0 <= i or 0 <= j:
            num = get_digit(a, i) + get_digit(b, j) + carry
            carry = num // self._BASE
            num %= self._BASE
            ans = f"{num}{ans}" str(n) + result
            i -= 1
            j -= 1

        if carry == 1:
            ans = '1' + ans
        return ans