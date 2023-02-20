// 576. Out of Boundary Paths

// Runtime: 6 ms, faster than 58.93% of Java online submissions for Out of Boundary Paths.

// Memory Usage: 39.5 MB, less than 20.31% of Java online submissions for Out of Boundary Paths.


class Solution {
    // Recursion with Memoization
    private final int MOD = 1000000007;

    private int[][][] ways;

    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        ways = new int[m][n][maxMove + 1];
        for (int[][] l : ways) {
            for (int[] sl : l) {
                Arrays.fill(sl, -1);
            }
        }

        return findPaths(maxMove, startRow, startColumn);
    }

    private int findPaths(int maxMove, int startRow, int startColumn) {
        if (startRow == ways.length || startColumn == ways[0].length || startRow < 0 || startColumn < 0) {
            return 1;
        } else if (maxMove == 0) {
            return 0;
        } else if (ways[startRow][startColumn][maxMove] >= 0) {
            return ways[startRow][startColumn][maxMove];
        } else {
            ways[startRow][startColumn][maxMove] = (
                (findPaths(maxMove - 1, startRow - 1, startColumn) + findPaths(maxMove - 1, startRow + 1, startColumn)) % MOD +
                (findPaths(maxMove - 1, startRow, startColumn - 1) + findPaths(maxMove - 1, startRow, startColumn + 1)) % MOD
            ) % MOD;

            return ways[startRow][startColumn][maxMove];
        }
    }
} 