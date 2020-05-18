// 70. Climbing Stairs

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Climbing Stairs.

// Memory Usage: 36.5 MB, less than 5.26% of Java online submissions for Climbing Stairs.


public class Solution {

    private int memo[] = null;

    // Recursion with Memoization
    public int climbStairs(int n) {
        memo = new int[n + 1];
        return _climbStairs(0, n);
    }

    public int _climbStairs(int curr, int dest) {
        if (curr > dest) {
            return 0;
        } else if (curr == dest) {
            return 1;
        } else if (memo[curr] > 0) {
            return memo[curr];
        }

        // Store the result at each step in `memo` array and directly returning the result from the `memo` array whenever that function is called again.
        memo[curr] = _climbStairs(curr + 1, dest) + _climbStairs(curr + 2, dest);
        return memo[curr];
    }
}