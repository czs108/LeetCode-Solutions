// 1. Two Sum

// Runtime: 55 ms, faster than 28.62% of Java online submissions for Two Sum.

// Memory Usage: 39.7 MB, less than 5.65% of Java online submissions for Two Sum.


class Solution {
    // Brute Force
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] == target - nums[i]) {
                    return new int[] { i, j };
                }
            }
        }

        throw new IllegalArgumentException("No two sum solution");
    }
}