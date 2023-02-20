# 435. Non-overlapping Intervals

# Time Limit Exceeded


class Solution:
    # Dynamic Programming Based on End Point
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()

        def overlapping(prev: int, curr: int) -> bool:
            return intervals[curr][0] < intervals[prev][1]

        # `valid_intervals` stores the maximum number of valid intervals
        # that can be included in the final list if the intervals upto the i-th interval only are considered, including itself.
        valid_intervals = [0] * len(intervals)
        valid_intervals[0] = 1
        for i in range(1, len(intervals)):
            for j in range(i - 1, -1, -1):
                if not overlapping(j, i):
                    valid_intervals[i] = valid_intervals[j] + 1
                    break
            valid_intervals[i] = max(valid_intervals[i], valid_intervals[i - 1])
        return len(intervals) - max(valid_intervals)