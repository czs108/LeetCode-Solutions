// 55. Jump Game


// We call a position in the array a "good index" if starting at that position, we can reach the last index.
// Otherwise, that index is called a "bad index".
enum Index {
    GOOD, BAD, UNKNOWN
}

class Solution {
    // Dynamic Programming - Top down
    private Index[] memo;

    public boolean canJump(int[] nums) {
        memo = new Index[nums.length];
        Arrays.fill(memo, Index.UNKNOWN);
        memo[memo.length - 1] = Index.GOOD;
        return canJumpFromPosition(0, nums);
    }

    private boolean canJumpFromPosition(int position, int[] nums) {
        if (memo[position] != Index.UNKNOWN) {
            return memo[position] == Index.GOOD ? true : false;
        }

        int furthestJump = Math.min(position + nums[position], nums.length - 1);
        for (int nextPosition = position + 1; nextPosition <= furthestJump; nextPosition++) {
            if (canJumpFromPosition(nextPosition, nums)) {
                memo[position] = Index.GOOD;
                return true;
            }
        }

        memo[position] = Index.BAD;
        return false;
    }
}