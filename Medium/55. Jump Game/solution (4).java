// 55. Jump Game

// Runtime: 1 ms, faster than 98.72% of Java online submissions for Jump Game.

// Memory Usage: 41.3 MB, less than 39.32% of Java online submissions for Jump Game.


// We call a position in the array a "good index" if starting at that position, we can reach the last index.
// Otherwise, that index is called a "bad index".
public class Solution {
    // Greedy
    public boolean canJump(int[] nums) {
        int lastPos = nums.length - 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            // If we can reach a GOOD index, then our position is itself GOOD.
            // Also, this new GOOD position will be the new leftmost GOOD index.
            if (i + nums[i] >= lastPos) {
                lastPos = i;
            }
        }

        return lastPos == 0;
    }
}