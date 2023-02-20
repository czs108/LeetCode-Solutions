// 322. Coin Change

// Runtime: 11 ms, faster than 87.34% of Java online submissions for Coin Change.

// Memory Usage: 39 MB, less than 5.33% of Java online submissions for Coin Change.


public class Solution {
    // Dynamic Programming - Bottom up
    public int coinChange(int[] coins, int amount) {
        int max = amount + 1;
        int[] count = new int[amount + 1];
        Arrays.fill(count, max);
        count[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (coins[j] <= i) {
                    count[i] = Math.min(count[i], count[i - coins[j]] + 1);
                }
            }
        }

        return count[amount] > amount ? -1 : count[amount];
    }
}