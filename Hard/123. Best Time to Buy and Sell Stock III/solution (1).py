# 123. Best Time to Buy and Sell Stock III

# Runtime: 172 ms, faster than 7.50% of Python3 online submissions for Best Time to Buy and Sell Stock III.

# Memory Usage: 22 MB, less than 9.09% of Python3 online submissions for Best Time to Buy and Sell Stock III.


import math

class Solution:
    STAGE_NUM = 5

    def maxProfit(self, prices: list[int]) -> int:
        # 5 stages:
        #   (0) Before the 1st buy.
        #       (1) Hold the 1st stock.
        #   (2) After the 1st sale, before the 2nd buy.
        #       (3) Hold the 2nd stock.
        #   (4) After the 2nd sale.
        profit = [[-math.inf for _ in range(Solution.STAGE_NUM)] for _ in range(len(prices) + 1)]
        profit[0][0] = 0

        for i in range(1, len(prices) + 1):
            # For the stage 0, 2, 4
            for j in range(0, Solution.STAGE_NUM, 2):
                # Did not hold the stock yesterday, and still do not buy it today.
                profit[i][j] = profit[i - 1][j]
                # Held the stock yesterday, but sell it today.
                if j > 0 and i >= 2 and not math.isinf(profit[i - 1][j - 1]):
                    curr_profit = prices[i - 1] - prices[i - 2]
                    profit[i][j] = max(profit[i][j], profit[i - 1][j - 1] + curr_profit)

            # For the stage 1, 3
            for j in range(1, Solution.STAGE_NUM, 2):
                # Did not hold the stock yesterday, but buy it today.
                profit[i][j] = profit[i - 1][j - 1]
                # Held the stock yesterday, and still hold it today.
                if i >= 2 and not math.isinf(profit[i - 1][j]):
                    curr_profit = prices[i - 1] - prices[i - 2]
                    profit[i][j] = max(profit[i][j], profit[i - 1][j] + curr_profit)
        return max(profit[-1][0], profit[-1][2], profit[-1][4])