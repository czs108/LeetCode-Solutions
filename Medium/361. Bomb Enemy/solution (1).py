# 361. Bomb Enemy

# Runtime: 736 ms, faster than 5.52% of Python3 online submissions for Bomb Enemy.

# Memory Usage: 19.4 MB, less than 7.54% of Python3 online submissions for Bomb Enemy.


class Solution:
    # Dynamic Programming
    def maxKilledEnemies(self, grid: list[list[str]]) -> int:
        Empty, Wall, Enemy = '0', 'W', 'E'
        if len(grid) == 0:
            return 0

        max_count = 0
        row_hits = 0
        col_hits = [0] * len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # Reset the hits on the row, if necessary.
                if col == 0 or grid[row][col - 1] == Wall:
                    row_hits = 0
                    for k in range(col, len(grid[0])):
                        if grid[row][k] == Wall:
                            # Stop the scan when we hit the wall.
                            break
                        elif grid[row][k] == Enemy:
                            row_hits += 1

                # Reset the hits on the column, if necessary.
                if row == 0 or grid[row - 1][col] == Wall:
                    col_hits[col] = 0
                    for k in range(row, len(grid)):
                        if grid[k][col] == Wall:
                            break
                        elif grid[k][col] == Enemy:
                            col_hits[col] += 1

                # Count the hits for each empty cell.
                if grid[row][col] == Empty:
                    total_hits = row_hits + col_hits[col]
                    max_count = max(max_count, total_hits)

        return max_count