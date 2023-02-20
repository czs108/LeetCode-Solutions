# 435. Non-overlapping Intervals

# Runtime: 1440 ms, faster than 48.92% of Python3 online submissions for Non-overlapping Intervals.

# Memory Usage: 52.5 MB, less than 57.63% of Python3 online submissions for Non-overlapping Intervals.


class Solution:
    # Greedy Approach Based on Starting Point
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()

        prev = 0
        count = 0
        # If two intervals are overlapping, we want to remove the interval that has the longer end point.
        # The longer interval will always overlap with more or the same number of future intervals compared to the shorter one.
        for i in range(1, len(intervals)):
            if intervals[prev][1] > intervals[i][0]:
                if intervals[prev][1] > intervals[i][1]:
                    # The two intervals currently considered are overlapping
                    # and the starting point of the later interval falls before the starting point of the previous interval.
                    prev = i
                else:
                    # The two intervals currently considered are overlapping
                    # and the end point of the later interval falls after the end point of the previous interval.
                    pass
                count += 1
            else:
                # The two intervals currently considered are non-overlapping.
                prev = i
        return count