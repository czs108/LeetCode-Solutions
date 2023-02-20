// 300. Longest Increasing Subsequence

// 21 / 24 test cases passed.
// Status: Time Limit Exceeded


class Solution {
    // Brute Force
    public int lengthOfLIS(int[] nums) {
        return lengthofLIS(nums, Integer.MIN_VALUE, 0);
    }

    private static int lengthofLIS(int[] nums, int prevVal, int currPos) {
        if (currPos == nums.length) {
            return 0;
        }

        int taken = 0;
        if (nums[currPos] > prevVal) {
            taken = 1 + lengthofLIS(nums, nums[currPos], currPos + 1);
        }

        int notTaken = lengthofLIS(nums, prevVal, currPos + 1);
        return Math.max(taken, notTaken);
    }
}