// 55. Jump Game


class Solution {
    // Backtracking
    public boolean canJump(int[] nums) {
        return canJumpFromPosition(0, nums);
    }

    private static boolean canJumpFromPosition(int position, int[] nums) {
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