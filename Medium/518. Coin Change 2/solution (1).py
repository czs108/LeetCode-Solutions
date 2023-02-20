# 518. Coin Change 2

# Runtime: 132 ms, faster than 96.13% of Python3 online submissions for Coin Change 2.

# Memory Usage: 14.3 MB, less than 85.53% of Python3 online submissions for Coin Change 2.


class Solution:
    # Dynamic Programming
    def change(self, amount: int, coins: list[int]) -> int:
        count = [0] * (amount + 1)
        count[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                count[x] += count[x - coin]
        return count[amount]