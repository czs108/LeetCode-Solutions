// 322. Coin Change

// Runtime: 32 ms, faster than 20.68% of Java online submissions for Coin Change.

// Memory Usage: 39.1 MB, less than 5.33% of Java online submissions for Coin Change.


public class Solution {

    private int[] count = null;

    // Dynamic Programming - Top down
    public int coinChange(int[] coins, int amount) {
        if (amount < 1) {
            return 0;
        } else {
            count = new int[amount]
            return _coinChange(coins, amount);
        }
    }

    private int _coinChange(int[] coins, int rem) {
        if (rem < 0) {
            return -1;
        } else if (rem == 0) {
            return 0;
        } else if (count[rem - 1] != 0) {
            return count[rem - 1];
        }

        int min = Integer.MAX_VALUE;
        for (int coin : coins) {
            int res = _coinChange(coins, rem - coin, count);
            if (res >= 0 && res < min) {
                min = 1 + res;
            }
        }

        count[rem - 1] = (min == Integer.MAX_VALUE) ? -1 : min;
        return count[rem - 1];
    }
}