// 300. Longest Increasing Subsequence

// Runtime: 11 ms, faster than 58.76% of Java online submissions for Longest Increasing Subsequence.

// Memory Usage: 37.5 MB, less than 34.00% of Java online submissions for Longest Increasing Subsequence.


class Solution {
    // Dynamic Programming
    public int lengthOfLIS(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        int[] count = new int[nums.length];
        count[0] = 1;

        int maxAns = 1;
        for (int i = 1; i < count.length; i++) {
            int maxVal = 0;
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    maxVal = Math.max(maxVal, count[j]);
                }
            }

            count[i] = maxVal + 1;
            maxAns = Math.max(maxAns, count[i]);
        }

        return maxAns;
    }
}