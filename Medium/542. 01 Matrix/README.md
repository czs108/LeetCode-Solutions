# 542. 01 Matrix

> Medium

------

Given an `m × n` binary matrix `mat`, return the distance of the nearest `0` for each cell.

The distance between two adjacent cells is `1`.

**Example 1:**

![mat-1](images/mat-1.jpg)

```
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
```

**Example 2:**

![mat-2](images/mat-2.jpg)

```
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
```

**Constraints:**

- `mat[i][j]` is either `0` or `1`.
- There is at least one `0` in `mat`.