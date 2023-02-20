# 56. Merge Intervals

# Runtime: 88 ms, faster than 62.23% of Python3 online submissions for Merge Intervals.

# Memory Usage: 16.3 MB, less than 10.54% of Python3 online submissions for Merge Intervals.


class Solution:
    # Sort
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # If the list of merged intervals is empty or if the current interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # Otherwise, there is overlap, so we merge the current and previous intervals.
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])
        return merged