# 63. Unique Paths II

# Runtime: 36 ms, faster than 98.27% of Python3 online submissions for Unique Paths II.

# Memory Usage: 13.6 MB, less than 8.89% of Python3 online submissions for Unique Paths II.


class Solution:
    # Dynamic programming
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0
        elif obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # Use the `obstacleGrid` array as the DP array thus not utilizing any additional space.

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1, m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)

        # Filling the values for the first row
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.
        return obstacleGrid[m - 1][n - 1]