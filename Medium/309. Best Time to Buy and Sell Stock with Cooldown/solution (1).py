# 309. Best Time to Buy and Sell Stock with Cooldown

# Runtime: 68 ms, faster than 18.79% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.

# Memory Usage: 14.6 MB, less than 62.61% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.


import math

class Solution:
    # Dynamic Programming with State Machine
    def maxProfit(self, prices: list[int]) -> int:
        sold, held, reset = -math.inf, -math.inf, 0
        for price in prices:
            prev_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, prev_sold)
        return max(sold, reset)
