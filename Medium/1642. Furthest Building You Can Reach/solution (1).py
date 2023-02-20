# 1642. Furthest Building You Can Reach


import heapq

class Solution:
    # Min Heap
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        # A min-heap.
        ladder_locs = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue

            # Allocate a ladder for this climb.
            heapq.heappush(ladder_locs, climb)
            # If we haven't gone over the number of ladders, nothing else to do.
            if len(ladder_locs) <= ladders:
                continue

            # Otherwise, we will need to take a climb out of `ladder_locs`.
            bricks -= heapq.heappop(ladder_locs)
            if bricks < 0:
                return i

        # If we got to here, this means we had enough to cover every climb.
        return len(heights) - 1