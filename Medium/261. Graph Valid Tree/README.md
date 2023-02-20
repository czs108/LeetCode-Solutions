# 261. Graph Valid Tree

> Medium

------

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [a_i, b_i]` indicates that there is an undirected edge between nodes `a_i` and `b_i` in the graph.

Return `true` if the edges of the given graph make up a valid tree, and `false` otherwise.

**Example 1:**

![graph-1](images/graph-1.jpg)

```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

**Example 2:**

![graph-2](images/graph-2.jpg)

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

Note that there are no self-loops or repeated edges.