# 7. Reverse Integer


class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(x)[::-1]) if x >= 0 else -int(str(x)[:0:-1])
        return res if -2**31 < res < 2**31 - 1 else 0