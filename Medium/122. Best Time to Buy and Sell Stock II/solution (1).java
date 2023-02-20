// 122. Best Time to Buy and Sell Stock II


class Solution {
    // Brute Force
    public int maxProfit(int[] prices) {
        return calculate(prices, 0);
    }

    private static int calculate(int prices[], int day) {
        if (day >= prices.length) {
            return 0;
        }

        int maxProfit = 0;
        for (int start = day; start < prices.length; start++) {
            int currMaxProfit = 0;
            for (int i = start + 1; i < prices.length; i++) {
                if (prices[start] < prices[i]) {
                    int profit = calculate(prices, i + 1) + prices[i] - prices[start];
                    currMaxProfit = Math.max(currMaxProfit, profit);
                }
            }

            maxProfit = Math.max(currMaxProfit, maxProfit);
        }

        return maxProfit;
    }
}