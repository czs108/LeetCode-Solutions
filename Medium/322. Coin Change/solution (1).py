# 322. Coin Change

# 15 / 182 test cases passed.
# Time Limit Exceeded


import sys

class Solution:
    # Recursive
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        count = sys.maxsize
        for n in coins:
            if amount >= n:
                remain = self.coinChange(coins, amount - n)
                if remain != -1:
                    count = min(remain + 1, count)
        return count if count != sys.maxsize else -1