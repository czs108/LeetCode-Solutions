// 70. Climbing Stairs

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Climbing Stairs.

// Memory Usage: 36.5 MB, less than 5.26% of Java online submissions for Climbing Stairs.


public class Solution {
    // Recursion with Memoization
    public int climbStairs(int n) {
        int memo[] = new int[n + 1];
        return climbStairs(0, n, memo);
    }

    public int climbStairs(int curr, int dest, int memo[]) {
        if (curr > dest) {
            return 0;
        } else if (curr == dest) {
            return 1;
        } else if (memo[curr] > 0) {
            return memo[curr];
        }

        // Store the result at each step in `memo` array and directly returning the result from the `memo` array whenever that function is called again.
        memo[curr] = climbStairs(curr + 1, dest, memo) + climbStairs(curr + 2, dest, memo);
        return memo[curr];
    }
}