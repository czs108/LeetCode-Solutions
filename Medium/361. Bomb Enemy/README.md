# 361. Bomb Enemy

> Medium

------

Given an `m × n` matrix `grid` where each cell is either a wall `'W'`, an enemy `'E'` or empty `'0'`, return the maximum enemies you can kill using one bomb. You can only place the bomb in an empty cell.

The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.

**Example 1:**

![grid-1](images/grid-1.jpg)

```
Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3
```

**Example 2:**

![grid-2](images/grid-2.jpg)

```
Input: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
Output: 1
```