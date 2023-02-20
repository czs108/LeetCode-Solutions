# 714. Best Time to Buy and Sell Stock with Transaction Fee

# Runtime: 942 ms, faster than 24.94% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.

# Memory Usage: 21.2 MB, less than 80.79% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.


import math

class Solution:
    # Dynamic Programming
    def maxProfit(self, prices: list[int], fee: int) -> int:
        hold, not_hold = -math.inf, 0
        for price in prices:
            hold = max(hold, not_hold - price)
            not_hold = max(not_hold, hold + price - fee)
        return not_hold