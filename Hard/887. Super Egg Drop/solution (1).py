# 887. Super Egg Drop

# Time Limit Exceeded


import math

class Solution:
    # Dynamic Programming
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
        for i in range(1, n + 1):
            # Drop at the floor `i`
            broken = self.superEggDrop(k - 1, i - 1)    # Search the floors [1, i - 1].
            not_broken = self.superEggDrop(k, n - i)    # Search the floors [i + 1, N].

            # Use `max` to find the worst case for each floor and use `min` to find the best option of floor.
            ret = min(ret, max(broken, not_broken) + 1)
        self._min_drop[k, n] = ret

        return self._min_drop[k, n]