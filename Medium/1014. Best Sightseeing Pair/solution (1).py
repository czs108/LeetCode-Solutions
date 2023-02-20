# 1014. Best Sightseeing Pair

# Runtime: 505 ms, faster than 46.50% of Python3 online submissions for Best Sightseeing Pair.

# Memory Usage: 19.9 MB, less than 19.68% of Python3 online submissions for Best Sightseeing Pair.


class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        max_left = 0 + values[0]
        best = 0
        for i in range(1, len(values)):
            best = max(best, max_left + values[i] - i)
            max_left = max(max_left, i + values[i])
        return best