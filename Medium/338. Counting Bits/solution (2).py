# 338. Counting Bits

# Runtime: 88 ms, faster than 60.45% of Python3 online submissions for Counting Bits.

# Memory Usage: 20.8 MB, less than 5.00% of Python3 online submissions for Counting Bits.


class Solution:
    # Dynamic Programming
    def countBits(self, num: int) -> list[int]:
        count = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            count[i] = count[i >> 1] + (i & 1)
        return count