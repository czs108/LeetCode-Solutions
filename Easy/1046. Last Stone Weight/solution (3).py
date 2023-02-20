# 1046. Last Stone Weight

# Runtime: 32 ms, faster than 70.58% of Python3 online submissions for Last Stone Weight.

# Memory Usage: 14.4 MB, less than 21.02% of Python3 online submissions for Last Stone Weight.


import heapq

class Solution:
    # Heap-Based Simulation
    def lastStoneWeight(self, stones: list[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            if stone1 != stone2:
                heapq.heappush(stones, stone1 - stone2)
        return -heapq.heappop(stones) if stones else 0