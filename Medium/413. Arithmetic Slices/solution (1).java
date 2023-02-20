// 413. Arithmetic Slices

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Arithmetic Slices.

// Memory Usage: 38.9 MB, less than 25.70% of Java online submissions for Arithmetic Slices.


class Solution {
    // Dynamic Programming
    public int numberOfArithmeticSlices(int[] nums) {
        int[] dp = new int[nums.length];
        int sum = 0;
        for (int i = 2; i < dp.length; i++) {
            if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
                dp[i] = 1 + dp[i - 1];
                sum += dp[i];
            }
        }

        return sum;
    }
}