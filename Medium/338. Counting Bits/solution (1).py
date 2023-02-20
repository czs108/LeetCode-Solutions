# 338. Counting Bits

# Runtime: 216 ms, faster than 9.27% of Python3 online submissions for Counting Bits.

# Memory Usage: 20.7 MB, less than 5.00% of Python3 online submissions for Counting Bits.


class Solution:
    def countBits(self, num: int) -> list[int]:
        count = []
        for i in range(num + 1):
            n = 0
            while i != 0:
                n += i & 1
                i >>= 1
            count.append(n)
        return count