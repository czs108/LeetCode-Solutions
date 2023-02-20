# 309. Best Time to Buy and Sell Stock with Cooldown

# Runtime: 2905 ms, faster than 5.04% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.

# Memory Usage: 14.6 MB, less than 62.61% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.


import math

class Solution:
    # Dynamic Programming
    def maxProfit(self, prices: list[int]) -> int:
        # `mp[i]` gives the maximal profits that we can gain for the price subsequence starting from the index `i`.
        # Padding the array with additional zero to simply the logic.
        mp = [0] * (len(prices) + 2)
        for i in range(len(prices) - 1, -1, -1):
            # Case 1: Buy and sell the current stock.
            c1 = 0
            for sell in range(i + 1, len(prices)):
                c1 = max(c1, prices[sell] - prices[i] + mp[sell + 2])

            # Case 2: Do no transaction with the current stock.
            c2 = mp[i + 1]
            mp[i] = max(c1, c2)
        return mp[0]