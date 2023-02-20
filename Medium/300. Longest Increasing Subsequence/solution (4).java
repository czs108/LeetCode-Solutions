// 300. Longest Increasing Subsequence

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Longest Increasing Subsequence.

// Memory Usage: 37.7 MB, less than 34.00% of Java online submissions for Longest Increasing Subsequence.


class Solution {
    // Dynamic Programming with Binary Search
    public int lengthOfLIS(int[] nums) {
        int[] count = new int[nums.length];
        int len = 0;
        for (int num : nums) {
            int i = Arrays.binarySearch(count, 0, len, num);
            if (i < 0) {
                i = -(i + 1);
            }

            count[i] = num;
            if (i == len) {
                len++;
            }
        }

        return len;
    }
}