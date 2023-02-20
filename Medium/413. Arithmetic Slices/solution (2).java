// 413. Arithmetic Slices

// Runtime: 1 ms, faster than 18.93% of Java online submissions for Arithmetic Slices.

// Memory Usage: 39.3 MB, less than 7.48% of Java online submissions for Arithmetic Slices.


class Solution {
    // Recursion
    private int sum = 0;

    public int numberOfArithmeticSlices(int[] nums) {
        slices(nums, nums.length - 1);
        return sum;
    }

    private int slices(int[] nums, int i) {
        if (i < 2) {
            return 0;
        }

        int ans = 0;
        if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
            ans = 1 + slices(nums, i - 1);
            sum += ans;
        } else {
            slices(nums, i - 1);
        }

        return ans;
    }
}