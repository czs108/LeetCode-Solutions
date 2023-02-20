// 300. Longest Increasing Subsequence


class Solution {
    // Recursion with Memoization
    // `memo[i][j]` represents the length of the LIS possible using `nums[i]` as the previous element considered to be included/not included in the LIS,
    // with `nums[j]` as the current element considered to be included/not included in the LIS.
    private int memo[][] = null;

    public int lengthOfLIS(int[] nums) {
        memo = new int[nums.length + 1][nums.length];
        for (int[] i : memo) {
            Arrays.fill(i, -1);
        }

        return lengthofLIS(nums, -1, 0);
    }

    private int lengthofLIS(int[] nums, int prevIdx, int currPos) {
        if (currPos == nums.length) {
            return 0;
        } else if (memo[prevIdx + 1][currPos] >= 0) {
            return memo[prevIdx + 1][currPos];
        }

        int taken = 0;
        if (prevIdx < 0 || nums[currPos] > nums[prevIdx]) {
            taken = 1 + lengthofLIS(nums, currPos, currPos + 1);
        }

        int notTaken = lengthofLIS(nums, prevIdx, currPos + 1);
        memo[prevIdx + 1][currPos] = Math.max(taken, notTaken);
        return memo[prevIdx + 1][currPos];
    }
}