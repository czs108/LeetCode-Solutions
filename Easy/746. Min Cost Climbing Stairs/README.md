# 746. Min Cost Climbing Stairs

> Easy

------

You are given an integer array `cost` where `cost[i]` is the cost of `i`-th step on a staircase. Once you pay the cost, you can either climb `1` or `2` steps.

You can either start from the step with index `0`, or the step with index `1`.

Return the minimum cost to reach the top of the floor.

**Example 1:**

```
Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
```

**Example 2:**

```
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
```