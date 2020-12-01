// 122. Best Time to Buy and Sell Stock II

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Best Time to Buy and Sell Stock II.

// Memory Usage: 39.9 MB, less than 11.43% of Java online submissions for Best Time to Buy and Sell Stock II.


class Solution {
    // Simple One Pass
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        // Go on crawling over the slope and keep on adding the profit obtained from every consecutive transaction.
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                maxProfit += prices[i] - prices[i - 1];
        }

        return maxProfit;
    }
}