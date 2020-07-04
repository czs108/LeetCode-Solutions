// 122. Best Time to Buy and Sell Stock II

// Runtime: 1 ms, faster than 93.45% of Java online submissions for Best Time to Buy and Sell Stock II.

// Memory Usage: 39.7 MB, less than 12.38% of Java online submissions for Best Time to Buy and Sell Stock II.


class Solution {
    // Peak Valley
    public int maxProfit(int[] prices) {
        if (prices.length == 0) {
            return 0;
        }

        int i = 0;
        int valley = prices[0];
        int peak = prices[0];
        int maxProfit = 0;
        // Find every peak immediately following every valley in the profit graph.
        while (i < prices.length - 1) {
            while (i < prices.length - 1 && prices[i] >= prices[i + 1]) {
                i++;
            }

            valley = prices[i];

            while (i < prices.length - 1 && prices[i] <= prices[i + 1]) {
                i++;
            }

            peak = prices[i];

            maxProfit += peak - valley;
        }

        return maxProfit;
    }
}