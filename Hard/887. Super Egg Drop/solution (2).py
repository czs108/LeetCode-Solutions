# 887. Super Egg Drop

# Runtime: 3096 ms, faster than 5.01% of Python3 online submissions for Super Egg Drop.

# Memory Usage: 16.1 MB, less than 63.53% of Python3 online submissions for Super Egg Drop.


import math

class Solution:
    # Dynamic Programming with Binary Search
    def __init__(self) -> None:
        self._min_drop = {}

    def superEggDrop(self, k: int, n: int) -> int:
        if k == 1:
            # Can only use linear scanning when having 1 egg.
            return n
        elif n == 0:
            return 0
        elif (k, n) in self._min_drop:
            return self._min_drop[k, n]

        ret = math.inf
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            # Drop at the floor `mid`
            broken = self.superEggDrop(k - 1, mid - 1)  # Search the floors [1, mid - 1].
            not_broken = self.superEggDrop(k, n - mid)  # Search the floors [mid + 1, N].
            if broken > not_broken:
                right = mid - 1
                ret = min(ret, broken + 1)
            else:
                left = mid + 1
                ret = min(ret, not_broken + 1)

        self._min_drop[k, n] = ret

        return self._min_drop[k, n]