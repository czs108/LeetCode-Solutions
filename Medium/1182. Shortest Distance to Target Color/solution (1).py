# 1182. Shortest Distance to Target Color

# Runtime: 2733 ms, faster than 23.80% of Python3 online submissions for Shortest Distance to Target Color.

# Memory Usage: 37.2 MB, less than 78.61% of Python3 online submissions for Shortest Distance to Target Color.


from collections import defaultdict
from bisect import bisect_left

class Solution:
    # HashMap & Binary Search
    def shortestDistanceColor(self, colors: list[int], queries: list[list[int]]) -> list[int]:
        color_pos = defaultdict(list)
        for i, c in enumerate(colors):
            color_pos[c].append(i)

        ans = []
        for i, (target, color) in enumerate(queries):
            if color not in color_pos:
                ans.append(-1)
                continue

            pos_list = color_pos[color]
            insert = bisect_left(pos_list, target)

            left_nearest = abs(pos_list[max(insert - 1, 0)] - target)
            right_nearest = abs(pos_list[min(insert, len(pos_list) - 1)] - target)
            ans.append(min(left_nearest, right_nearest))

        return ans