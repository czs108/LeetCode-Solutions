// 70. Climbing Stairs

// 21 / 45 test cases passed.
// Status: Time Limit Exceeded


public class Solution {
    // Brute Force
    public int climbStairs(int n) {
        return climbStairs(0, n);
    }

    public static int climbStairs(int curr, int dest) {
        if (curr > dest) {
            return 0;
        } else if (curr == dest) {
            return 1;
        } else {
            return climbStairs(curr + 1, dest) + climbStairs(curr + 2, dest);
        }
    }
}