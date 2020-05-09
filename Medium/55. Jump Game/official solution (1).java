// 55. Jump Game


class Solution {
    // Backtracking
    public boolean canJump(int[] nums) {
        assert(1 <= nums.length && nums.length <= 3 * 10000);
        return canJumpFromPosition(0, nums);
    }

    private boolean canJumpFromPosition(int position, int[] nums) {
        assert(1 <= nums.length && nums.length <= 3 * 10000);
        if (position == nums.length - 1) {
            return true;
        }

        // Start from the first position and jump to every index that is reachable.
        int furthestJump = Math.min(position + nums[position], nums.length - 1);
        // Try to make the biggest jump such that we reach the end as soon as possible.
        for (int nextPosition = furthestJump; nextPosition > position; nextPosition--) {
            if (canJumpFromPosition(nextPosition, nums)) {
                return true;
            }
        }

        return false;
    }
}