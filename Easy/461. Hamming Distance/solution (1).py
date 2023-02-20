# 461. Hamming Distance


class Solution:
    # Bit Shift
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        dist = 0
        while xor:
            if xor & 1:
                dist += 1
            xor >>= 1
        return dist