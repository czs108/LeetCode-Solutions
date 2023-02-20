# 1642. Furthest Building You Can Reach

# Runtime: 1118 ms, faster than 13.48% of Python3 online submissions for Furthest Building You Can Reach.

# Memory Usage: 28.7 MB, less than 33.04% of Python3 online submissions for Furthest Building You Can Reach.


import heapq

class Solution:
    # Max Heap
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        # A max-heap.
        brick_locs = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue

            # Allocate bricks for this climb.
            heapq.heappush(brick_locs, -climb)
            bricks -= climb

            # If we've used all the bricks, and have no ladders remaining, then we can't go any further.
            if bricks < 0 and ladders == 0:
                return i
            elif bricks < 0:
                bricks += -heapq.heappop(brick_locs)
                ladders -= 1

        # If we got to here, this means we had enough to cover every climb.
        return len(heights) - 1