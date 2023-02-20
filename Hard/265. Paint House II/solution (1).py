# 265. Paint House II

# Runtime: 236 ms, faster than 19.40% of Python3 online submissions for Paint House II.

# Memory Usage: 14.2 MB, less than 84.95% of Python3 online submissions for Paint House II.


import math

class Solution:
    # Dynamic Programming
    def minCostII(self, costs: list[list[int]]) -> int:
        if not costs:
            return 0

        for i in range(1, len(costs)):
            for c1 in range(len(costs[0])):
                cost = math.inf
                for c2 in range(len(costs[0])):
                    if c2 != c1:
                        cost = min(cost, costs[i - 1][c2])
                costs[i][c1] += cost
        return min(costs[-1])