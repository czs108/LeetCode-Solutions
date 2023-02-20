// 296. Best Meeting Point

// Time Limit Exceeded


class Solution {
    // Manhattan Distance Formula
    public int minTotalDistance(int[][] grid) {
        List<Point> points = getAllPoints(grid);
        int minDistance = Integer.MAX_VALUE;
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {
                int distance = calculateDistance(points, row, col);
                minDistance = Math.min(distance, minDistance);
            }
        }

        return minDistance;
    }

    private int calculateDistance(List<Point> points, int row, int col) {
        int distance = 0;
        for (Point point : points) {
            distance += Math.abs(point.row - row) + Math.abs(point.col - col);
        }

        return distance;
    }

    private List<Point> getAllPoints(int[][] grid) {
        List<Point> points = new ArrayList<>();
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {
                if (grid[row][col] == 1) {
                    points.add(new Point(row, col));
                }
            }
        }

        return points;
    }

    public class Point {
        int row;
        int col;

        public Point(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
}