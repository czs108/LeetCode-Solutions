# 1314. Matrix Block Sum

> Medium

------

Given a `m × n` matrix `mat` and an integer `k`, return a matrix `answer` where each `answer[i][j]` is the sum of all elements `mat[r][c]` for:

- `i - k ≤ r ≤ i + k`
- `j - k ≤ c ≤ j + k`
- `(r, c)` is a valid position in the matrix.

**Example 1:**

```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
```

**Example 2:**

```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
```