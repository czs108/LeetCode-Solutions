# 461. Hamming Distance

# Runtime: 32 ms, faster than 69.29% of Python3 online submissions for Hamming Distance.

# Memory Usage: 14.1 MB, less than 73.96% of Python3 online submissions for Hamming Distance.


class Solution:
    # Brian Kernighan's Algorithm
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        dist = 0
        while xor:
            xor &= (xor - 1)
            dist += 1
        return dist