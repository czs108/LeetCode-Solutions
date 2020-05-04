// 26. Remove Duplicates from Sorted Array

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Remove Duplicates from Sorted Array.

// Memory Usage: 41.3 MB, less than 21.81% of Java online submissions for Remove Duplicates from Sorted Array.


class Solution {
    // Two Pointers
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
             return 0;
        }

        int len = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[len]) {
                len++;
                nums[len] = nums[i];
            }
        }

        return len + 1;
    }
}