# 98. Validate Binary Search Tree

> Medium

------

Given the `root` of a binary tree, determine if it is a valid binary search tree.

A valid binary search tree is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**

![tree-1](images/tree-1.jpg)

```
Input: root = [2,1,3]
Output: true
```

**Example 2:**

![tree-2](images/tree-2.jpg)

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```