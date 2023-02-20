# 289. Game of Life

> Medium

------

According to the Wikipedia: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a `board` with `m × n` cells, each cell has an initial state `live` (`1`) or `dead` (`0`). Each cell interacts with its `8` neighbors using the following four rules:

- Any live cell with fewer than `2` live neighbors dies, as if caused by under-population.
- Any live cell with `2` or `3` live neighbors lives on to the next generation.
- Any live cell with more than `3` live neighbors dies, as if by over-population.
- Any dead cell with exactly `3` live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

**Example:**

```
Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
```