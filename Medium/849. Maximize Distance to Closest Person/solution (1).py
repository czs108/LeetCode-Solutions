# 849. Maximize Distance to Closest Person

# Runtime: 241 ms, faster than 10.24% of Python3 online submissions for Maximize Distance to Closest Person.

# Memory Usage: 14.7 MB, less than 77.02% of Python3 online submissions for Maximize Distance to Closest Person.


import math

class Solution:
    # Two Pointers
    def maxDistToClosest(self, seats: list[int]) -> int:
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)
                left = math.inf if prev is None else i - prev
                right = math.inf if future is None else future - i
                ans = max(ans, min(left, right))
        return ans