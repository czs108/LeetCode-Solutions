// 296. Best Meeting Point

// Time Limit Exceeded


class Solution {
    // Breadth-first Search
    public int minTotalDistance(int[][] grid) {
        int minDistance = Integer.MAX_VALUE;
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {
                int distance = search(grid, row, col);
                minDistance = Math.min(distance, minDistance);
            }
        }

        return minDistance;
    }

    private int search(int[][] grid, int row, int col) {
        Queue<Point> q = new LinkedList<>();
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        q.add(new Point(row, col, 0));
        int totalDistance = 0;
        while (!q.isEmpty()) {
            Point point = q.poll();
            int r = point.row;
            int c = point.col;
            int d = point.distance;
            if (r < 0 || c < 0 || r >= m || c >= n || visited[r][c]) {
                continue;
            }
            if (grid[r][c] == 1) {
                totalDistance += d;
            }
            visited[r][c] = true;
            q.add(new Point(r + 1, c, d + 1));
            q.add(new Point(r - 1, c, d + 1));
            q.add(new Point(r, c + 1, d + 1));
            q.add(new Point(r, c - 1, d + 1));
        }

        return totalDistance;
    }

    public class Point {
        int row;
        int col;
        int distance;

        public Point(int row, int col, int distance) {
            this.row = row;
            this.col = col;
            this.distance = distance;
        }
    }
}