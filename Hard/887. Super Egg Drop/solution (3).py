# 887. Super Egg Drop

# Runtime: 172 ms, faster than 51.90% of Python3 online submissions for Super Egg Drop.

# Memory Usage: 20.7 MB, less than 58.32% of Python3 online submissions for Super Egg Drop.


class Solution:
    # Dynamic Programming
    def superEggDrop(self, k: int, n: int) -> int:
        # We can test a building having `max_floor[i][j]` floors with `i` eggs and `j` tries.
        max_floor = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

        tries = 0
        while max_floor[k][tries] < n:
            tries += 1
            for i in range(1, k + 1):
                broken = max_floor[i - 1][tries - 1]
                not_broken = max_floor[i][tries - 1]
                max_floor[i][tries] = broken + not_broken + 1

        return tries