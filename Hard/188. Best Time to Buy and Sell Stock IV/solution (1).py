# 188. Best Time to Buy and Sell Stock IV

# Runtime: 468 ms, faster than 5.01% of Python3 online submissions for Best Time to Buy and Sell Stock IV.

# Memory Usage: 21.2 MB, less than 16.67% of Python3 online submissions for Best Time to Buy and Sell Stock IV.


import math

class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:

        def max_profit_without_limit() -> int:
            # 122. Best Time to Buy and Sell Stock II
            max_profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit

        if len(prices) == 0:
            return 0
        elif k > len(prices) // 2:
            return max_profit_without_limit

        # Stages are from 0 to 2k.
        # Do not hold the stock in stage 0, 2, 4...
        # Hold the stock in stage 1, 3, 5...
        stage_num = 2 * k + 1
        profit = [[-math.inf for _ in range(stage_num)] for _ in range(len(prices) + 1)]
        profit[0][0] = 0

        for i in range(1, len(prices) + 1):
            # For the stage 0, 2, 4...
            for j in range(0, stage_num, 2):
                # Did not hold the stock yesterday, and still do not buy it today.
                profit[i][j] = profit[i - 1][j]
                # Held the stock yesterday, but sell it today.
                if j > 0 and i >= 2 and not math.isinf(profit[i - 1][j - 1]):
                    curr_profit = prices[i - 1] - prices[i - 2]
                    profit[i][j] = max(profit[i][j], profit[i - 1][j - 1] + curr_profit)

            # For the stage 1, 3, 5...
            for j in range(1, stage_num, 2):
                # Did not hold the stock yesterday, but buy it today.
                profit[i][j] = profit[i - 1][j - 1]
                # Held the stock yesterday, and still hold it today.
                if i >= 2 and not math.isinf(profit[i - 1][j]):
                    curr_profit = prices[i - 1] - prices[i - 2]
                    profit[i][j] = max(profit[i][j], profit[i - 1][j] + curr_profit)

        max_profit = 0
        for i in range(0, stage_num, 2):
            max_profit = max(max_profit, profit[-1][i])
        return max_profit