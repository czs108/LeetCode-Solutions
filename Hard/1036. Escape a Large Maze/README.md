# 1036. Escape a Large Maze

> Hard

------

In a `1000000 × 1000000` grid, the coordinates of each grid square are `(x, y)` with `0 ≤ x, y ＜ 1000000`.

We start at the `source` square and want to reach the `target` square. Each move, we can walk to a 4-directionally adjacent square in the grid that isn't in the given list of `blocked` squares.

Return `true` if and only if it is possible to reach the target square through a sequence of moves.

**Example 1:**

```
Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation:
The target square is inaccessible starting from the source square, because we can't walk outside the grid.
```

**Example 2:**

```
Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation:
Because there are no blocked cells, it's possible to reach the target square.
```