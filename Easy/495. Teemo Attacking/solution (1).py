# 495. Teemo Attacking

# Runtime: 374 ms, faster than 11.31% of Python3 online submissions for Teemo Attacking.

# Memory Usage: 15.5 MB, less than 44.99% of Python3 online submissions for Teemo Attacking.


class Solution:
    # One Pass
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total = 0
        for i in range(1, len(timeSeries)):
            total += min(duration, timeSeries[i] - timeSeries[i - 1])
        return total + duration