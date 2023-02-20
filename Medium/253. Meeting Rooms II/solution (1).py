# 253. Meeting Rooms II


import heapq

class Solution:
    # Priority Queues
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        end_times = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(end_times, intervals[0][1])

        for interval in intervals[1:]:
            # If the room due to free up the earliest is free, assign that room to this meeting.
            if end_times[0] <= interval[0]:
                heapq.heappop(end_times)
                       # If a new room is to be assigned, then also we add to the heap.
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(end_times, interval[1])

        return len(end_times)