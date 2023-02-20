# 212. Word Search II

> Hard

------

Given an `m × n` board of characters and a list of strings `words`, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

**Example 1:**

![grid-1](images/grid-1.jpg)

```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

**Example 2:**

![grid-2](images/grid-2.jpg)

```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

**Constraints:**

- All the strings of `words` are unique.
- `words[i]` consists of lowercase English letters.