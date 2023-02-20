# 994. Rotting Oranges

# Runtime: 56 ms, faster than 50.05% of Python3 online submissions for Rotting Oranges.

# Memory Usage: 14.1 MB, less than 88.54% of Python3 online submissions for Rotting Oranges.


from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        Fresh, Rotten = 1, 2

        que = deque()
        fresh_num = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == Rotten:
                    que.append((row, col))
                elif grid[row][col] == Fresh:
                    fresh_num += 1
        que.append((-1, -1))

        time = -1
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        while que:
            row, col = que.popleft()
            if row < 0:
                time += 1
                if que:
                    que.append((-1, -1))
            else:
                for dir in dirs:
                    next_row, next_col = row + dir[0], col + dir[1]
                    if 0 <= next_row and next_row < len(grid) and 0 <= next_col and next_col < len(grid[0]):
                        if grid[next_row][next_col] == Fresh:
                            grid[next_row][next_col] = Rotten
                            que.append((next_row, next_col))
                            fresh_num -= 1
        return time if fresh_num == 0 else -1
