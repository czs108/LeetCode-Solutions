# 70. Climbing Stairs


class Solution:
    # Recursion with Memoization
    def __init__(self) -> None:
        self._mem: list[int] = None

    def climbStairs(self, n: int) -> int:
        self._mem = [-1 for _ in range(n + 1)]
        return self._climb_stairs(n)

    def _climb_stairs(self, n: int) -> int:
        if n < 0:
            return 0
        elif n == 0 or n == 1:
            return 1
        elif self._mem[n] >= 0:
            return self._mem[n]
        else:
            self._mem[n] = self._climb_stairs(n - 1) + self._climb_stairs(n - 2)
            return self._mem[n]