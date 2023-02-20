# 1130. Minimum Cost Tree From Leaf Values

# Runtime: 304 ms, faster than 16.66% of Python3 online submissions for Minimum Cost Tree From Leaf Values.

# Memory Usage: 14.9 MB, less than 9.62% of Python3 online submissions for Minimum Cost Tree From Leaf Values.


import math

class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        if len(arr) == 0:
            return 0

        sums = [[0] * len(arr) for _ in range(len(arr))]

        def get_min_sum(start: int, end: int) -> int:
            if start >= end:
                return 0
            elif sums[start][end] > 0:
                return sums[start][end]

            min_sum = math.inf
            for i in range(start, end):
                min_sum = min(min_sum, get_min_sum(start, i) + get_min_sum(i + 1, end) + max(arr[start:i + 1]) * max(arr[i + 1:end + 1]))
            sums[start][end] = min_sum
            return min_sum

        return get_min_sum(0, len(arr) - 1)