// 221. Maximal Square

// Runtime: 9 ms, faster than 24.48% of Java online submissions for Maximal Square.

// Memory Usage: 48.7 MB, less than 20.74% of Java online submissions for Maximal Square.


class Solution {
    // Dynamic Programming
    public int maximalSquare(char[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        // `dp(i,j)` represents the side length of the maximum square whose bottom-right corner is the cell with index (i,j) in the original matrix.
        int[][] dp = new int[rows + 1][cols + 1];

        int maxSqLen = 0;
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                if (matrix[i - 1][j - 1] == '1'){
                    dp[i][j] = Math.min(Math.min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1;
                    maxSqLen = Math.max(maxSqLen, dp[i][j]);
                }
            }
        }

        return maxSqLen * maxSqLen;
    }
}