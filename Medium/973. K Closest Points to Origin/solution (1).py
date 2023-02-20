# 973. K Closest Points to Origin

# Runtime: 680 ms, faster than 72.15% of Python3 online submissions for K Closest Points to Origin.

# Memory Usage: 20.1 MB, less than 44.16% of Python3 online submissions for K Closest Points to Origin.


import heapq

class Solution:
    # Heap
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return heapq.nsmallest(k, points, lambda p: p[0]**2 + p[1]**2)