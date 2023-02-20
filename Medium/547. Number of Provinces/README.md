# 547. Number of Provinces

> Medium

------

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n × n` matrix `isConnected` where `isConnected[i][j] = 1` if the `i`-th city and the `j`-th city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return the total number of provinces.

**Example 1:**

![graph-1](images/graph-1.jpg)

```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

**Example 2:**

![graph-2](images/graph-2.jpg)

```
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```