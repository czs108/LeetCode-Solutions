# 253. Meeting Rooms II

# Runtime: 76 ms, faster than 78.95% of Python3 online submissions for Meeting Rooms II.

# Memory Usage: 17.6 MB, less than 23.48% of Python3 online submissions for Meeting Rooms II.


class Solution:
    # Chronological Ordering
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        count = 0
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        start, end = 0, 0
        while start < len(intervals):
            # If there is a meeting that has ended by the time the meeting at `start` starts.
            if start_times[start] >= end_times[end]:
                # Do not need a new room.
                end += 1
            else:
                count += 1
            start += 1
        return count