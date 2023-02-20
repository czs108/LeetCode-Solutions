# 121. Best Time to Buy and Sell Stock

# Runtime: 1144 ms, faster than 37.36% of Python3 online submissions for Best Time to Buy and Sell Stock.

# Memory Usage: 25.2 MB, less than 52.13% of Python3 online submissions for Best Time to Buy and Sell Stock.


class Solution:
    # Dynamic Programming
    def maxProfit(self, prices: list[int]) -> int:
        buy, sell = prices[0], 0
        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            sell = max(sell, prices[i] - buy)
        return sell