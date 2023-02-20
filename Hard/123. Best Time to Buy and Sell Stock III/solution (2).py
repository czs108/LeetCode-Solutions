# 123. Best Time to Buy and Sell Stock III

# Runtime: 96 ms, faster than 29.25% of Python3 online submissions for Best Time to Buy and Sell Stock III.

# Memory Usage: 15.2 MB, less than 45.45% of Python3 online submissions for Best Time to Buy and Sell Stock III.


import math

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_1_sell_0 = -math.inf
        buy_1_sell_1 = 0
        buy_2_sell_1 = -math.inf
        buy_2_sell_2 = 0
        for price in prices:
            buy_2_sell_2 = max(buy_2_sell_2, buy_2_sell_1 + price)
            buy_2_sell_1 = max(buy_2_sell_1, buy_1_sell_1 - price)
            buy_1_sell_1 = max(buy_1_sell_1, buy_1_sell_0 + price)
            buy_1_sell_0 = max(buy_1_sell_0, -price)
        return max(buy_1_sell_1, buy_2_sell_2)