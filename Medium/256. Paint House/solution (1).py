# 256. Paint House

# Runtime: 68 ms, faster than 42.13% of Python3 online submissions for Paint House.

# Memory Usage: 14.9 MB, less than 7.26% of Python3 online submissions for Paint House.


class Solution:
    # Recursive Tree
    def minCost(self, costs: list[list[int]]) -> int:
        Red, Green, Blue = 0, 1, 2
        memo = {}

        def paint_cost(n: int, color: int) -> int:
            if (n, color) in memo:
                return memo[(n, color)]
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == Red:
                total_cost += min(paint_cost(n + 1, Green), paint_cost(n + 1, Blue))
            elif color == Green:
                total_cost += min(paint_cost(n + 1, Red), paint_cost(n + 1, Blue))
            else:
                total_cost += min(paint_cost(n + 1, Red), paint_cost(n + 1, Green))
            memo[(n, color)] = total_cost
            return total_cost

        if not costs:
            return 0
        else:
            return min(paint_cost(0, Red), paint_cost(0, Green), paint_cost(0, Blue))