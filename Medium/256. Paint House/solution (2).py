# 256. Paint House

# Runtime: 56 ms, faster than 88.75% of Python3 online submissions for Paint House.

# Memory Usage: 14.2 MB, less than 92.94% of Python3 online submissions for Paint House.


class Solution:
    # Dynamic Programming
    def minCost(self, costs: list[list[int]]) -> int:
        if not costs:
            return 0

        Red, Green, Blue = 0, 1, 2
        for i in range(1, len(costs)):
            costs[i][Red] += min(costs[i - 1][Blue], costs[i - 1][Green])
            costs[i][Green] += min(costs[i - 1][Red], costs[i - 1][Blue])
            costs[i][Blue] += min(costs[i - 1][Red], costs[i - 1][Green])
        return min(costs[-1])