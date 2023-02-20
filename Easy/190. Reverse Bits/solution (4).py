# 190. Reverse Bits


class Solution:
    def reverseBits(self, n: int) -> int:
        ans, power = 0, 31
        while n:
            ans += (n & 1) << power
            power -= 1
            n >>= 1
        return ans