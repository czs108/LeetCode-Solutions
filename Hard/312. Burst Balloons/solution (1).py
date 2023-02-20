# 312. Burst Balloons

# Runtime: 8448 ms, faster than 44.62% of Python3 online submissions for Burst Balloons.

# Memory Usage: 19.9 MB, less than 38.33% of Python3 online submissions for Burst Balloons.


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        # Edge case
        nums = [1] + nums + [1]
        scores = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        for i in range(n, -1, -1):
            for j in range(i + 1, n + 2):
                # The last burst.
                for k in range(i + 1, j):
                    scores[i][j] = max(scores[i][j], scores[i][k] + scores[k][j] + nums[i] * nums[k] * nums[j])

        return scores[0][n + 1]