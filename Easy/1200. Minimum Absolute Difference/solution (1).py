# 1200. Minimum Absolute Difference

# Runtime: 340 ms, faster than 69.62% of Python3 online submissions for Minimum Absolute Difference.

# Memory Usage: 28.1 MB, less than 60.76% of Python3 online submissions for Minimum Absolute Difference.


import math

class Solution:
    # Sorting
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        min_diff, res = math.inf, []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] < min_diff:
                min_diff = arr[i] - arr[i - 1]
                res = []
            if arr[i] - arr[i - 1] == min_diff:
                res.append([arr[i - 1], arr[i]])
        return res