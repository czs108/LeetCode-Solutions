# 124. Binary Tree Maximum Path Sum

> Hard

------

Given a **non-empty** binary tree, find the maximum path sum.

For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain **at least one node** and does not need to go through the root.

**Example 1:**

![tree (1)](Images/tree (1).jpg)

```
Input: root = [1,2,3]
Output: 6
```

**Example 2:**

![tree (2)](Images/tree (2).jpg)

```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
```

**Constraints:**

- The number of nodes in the tree is in the range [0, 3 * 10<sup>4</sup>].
- `-1000 <= Node.val <= 1000`