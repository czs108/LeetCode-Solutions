// 217. Contains Duplicate

// Runtime: 3 ms, faster than 99.68% of Java online submissions for Contains Duplicate.

// Memory Usage: 43.3 MB, less than 82.76% of Java online submissions for Contains Duplicate.


class Solution {
    // Sorting
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; ++i) {
            if (nums[i] == nums[i + 1]) {
                return true;
            }
        }

        return false;
    }
}