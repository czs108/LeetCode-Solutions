# 746. Min Cost Climbing Stairs

# Runtime: 56 ms, faster than 78.65% of Python3 online submissions for Min Cost Climbing Stairs.

# Memory Usage: 14.6 MB, less than 17.69% of Python3 online submissions for Min Cost Climbing Stairs.


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost_sums = [0 for _ in range(len(cost) + 1)]
        for i in range(2, len(cost) + 1):
            one_step = cost_sums[i - 1] + cost[i - 1]
            two_step = cost_sums[i - 2] + cost[i - 2]
            cost_sums[i] = min(one_step, two_step)
        return cost_sums[-1]