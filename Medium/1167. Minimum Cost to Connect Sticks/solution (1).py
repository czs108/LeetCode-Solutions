# 1167. Minimum Cost to Connect Sticks


import heapq

class Solution:
    # Greedy | Heap
    def connectSticks(self, sticks: list[int]) -> int:
        heapq.heapify(sticks)

        cost = 0
        while len(sticks) > 1:
            # Always pick two of the smallest sticks to connect.
            stick1, stick2 = heapq.heappop(sticks), heapq.heappop(sticks)
            cost += stick1 + stick2
            heapq.heappush(sticks, stick1 + stick2)
        return cost