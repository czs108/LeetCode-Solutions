# 1629. Slowest Key

# Runtime: 48 ms, faster than 96.02% of Python3 online submissions for Slowest Key.

# Memory Usage: 14.4 MB, less than 81.38% of Python3 online submissions for Slowest Key.


class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        key = keysPressed[0]
        max_duration = releaseTimes[0]
        prev_rls_time = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - prev_rls_time
            if duration > max_duration or (duration == max_duration and keysPressed[i] > key):
                max_duration = duration
                key = keysPressed[i]
            prev_rls_time = releaseTimes[i]
        return key