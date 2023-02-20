# 1046. Last Stone Weight

# Runtime: 28 ms, faster than 88.82% of Python3 online submissions for Last Stone Weight.

# Memory Usage: 14.3 MB, less than 51.84% of Python3 online submissions for Last Stone Weight.


import bisect

class Solution:
    # Sorted Array-Based Simulation
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stone1, stone2 = stones.pop(), stones.pop()
            if stone1 != stone2:
                bisect.insort(stones, stone1 - stone2)
        return stones[0] if stones else 0