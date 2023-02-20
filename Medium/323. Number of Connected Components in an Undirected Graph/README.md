# 323. Number of Connected Components in an Undirected Graph

> Medium

------

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [a_i, b_i]` indicates that there is an undirected edge between nodes `a_i` and `b_i` in the graph.

Return the number of connected components in the graph.

**Example 1:**

![graph-1](images/graph-1.jpg)

```
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
```

**Example 2:**

![graph-2](images/graph-2.jpg)

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
```

Note that there are no repeated edges.