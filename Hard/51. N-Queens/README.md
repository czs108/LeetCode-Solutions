# 51. N-Queens

> Hard

------

The `n`-queens puzzle is the problem of placing `n` queens on an `n × n` chessboard such that no two queens attack each other.

Given an integer `n`, return all distinct solutions to the `n`-queens puzzle.

Each solution contains a distinct board configuration of the `n`-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space respectively.

**Example 1:**

![4-queens](images/4-queens.jpg)

```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

**Example 2:**

```
Input: n = 1
Output: [["Q"]]
```