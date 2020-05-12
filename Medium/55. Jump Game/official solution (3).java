// 55. Jump Game

// Runtime: 237 ms, faster than 27.27% of Java online submissions for Jump Game.

// Memory Usage: 41 MB, less than 50.43% of Java online submissions for Jump Game.


// We call a position in the array a "good index" if starting at that position, we can reach the last index.
// Otherwise, that index is called a "bad index".
enum Index {
    GOOD, BAD, UNKNOWN
}

public class Solution {
    // Dynamic Programming - Bottom up
    public boolean canJump(int[] nums) {
        Index[] memo = new Index[nums.length];
        Arrays.fill(memo, Index.UNKNOWN);
        memo[memo.length - 1] = Index.GOOD;

        for (int i = nums.length - 2; i >= 0; i--) {
            int furthestJump = Math.min(i + nums[i], nums.length - 1);
            for (int j = i + 1; j <= furthestJump; j++) {
                if (memo[j] == Index.GOOD) {
                    memo[i] = Index.GOOD;
                    break;
                }
            }
        }

        return memo[0] == Index.GOOD;
    }
}