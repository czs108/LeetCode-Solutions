// 121. Best Time to Buy and Sell Stock

// Runtime: 1 ms, faster than 99.20% of Java online submissions for Best Time to Buy and Sell Stock.

// Memory Usage: 39.8 MB, less than 10.17% of Java online submissions for Best Time to Buy and Sell Stock.


class Solution {
    // One Pass
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        // Find the largest peak following the smallest valley in the profit graph.
        for (int i = 0; i < prices.length; i++) {
            minPrice = Math.min(minPrice, prices[i]);
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }

        return maxProfit;
    }
}