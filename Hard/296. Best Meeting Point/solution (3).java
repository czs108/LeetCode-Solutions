// 296. Best Meeting Point

// Runtime: 25 ms, faster than 14.44% of Java online submissions for Best Meeting Point.

// Memory Usage: 46.6 MB, less than 6.77% of Java online submissions for Best Meeting Point.


class Solution {
    // Sorting
    // As long as there is equal number of points to the left and right of the meeting point, the total distance is minimized.
    //
    // Why:
    // For the case: 1-1-0-0-1. The median `x` = 1 is our initial meeting point.
    // Now if we move one step to its right where `x` = 2. Assume that the total distance traveled is `d`.
    // Since there are two points to the left of `x` = 2, we add 2 * (+1) to `d`.
    // And `d` is offset by –1 since there is one point to the right.
    // This means the distance had overall increased by 1.
    public int minTotalDistance(int[][] grid) {
        List<Integer> rows = new ArrayList<>();
        List<Integer> cols = new ArrayList<>();
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {
                if (grid[row][col] == 1) {
                    rows.add(row);
                    cols.add(col);
                }
            }
        }

        int row = rows.get(rows.size() / 2);
        Collections.sort(cols);
        int col = cols.get(cols.size() / 2);
        return minDistance1D(rows, row) + minDistance1D(cols, col);
    }

    private int minDistance1D(List<Integer> points, int origin) {
        int distance = 0;
        for (int point : points) {
            distance += Math.abs(point - origin);
        }

        return distance;
    }
}