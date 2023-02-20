# 746. Min Cost Climbing Stairs

# Runtime: 64 ms, faster than 35.45% of Python3 online submissions for Min Cost Climbing Stairs.

# Memory Usage: 16.1 MB, less than 9.35% of Python3 online submissions for Min Cost Climbing Stairs.


class Solution:
    # Top-Down Dynamic Programming
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost_sums = [0 for _ in range(len(cost) + 1)]

        def climb_to(n: int) -> int:
            if n == 0 or n == 1:
                return 0
            elif cost_sums[n] > 0:
                return cost_sums[n]
            else:
                one_step = climb_to(n - 1) + cost[n - 1]
                two_step = climb_to(n - 2) + cost[n - 2]
                cost_sums[n] = min(one_step, two_step)
                return cost_sums[n]

        return climb_to(len(cost))