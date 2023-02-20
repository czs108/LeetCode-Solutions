# 1217. Minimum Cost to Move Chips to The Same Position

# Runtime: 36 ms, faster than 41.44% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.

# Memory Usage: 14.3 MB, less than 51.59% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.


class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        # Move all chips at even positions to position 0.
        # Move all chips at odd positions to position 1.
        even_count = 0
        odd_count = 0
        for i in position:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return min(even_count, odd_count)