# 285. Inorder Successor in BST

> Medium

------

Given the `root` of a Binary Search Tree (BST) and a node `p` in it, return the inorder successor of that node in the BST. If the given node has no inorder successor in the tree, return `null`.

The successor of a node `p` is the node with the smallest key greater than `p.val`.

**Example 1:**

![tree-1](images/tree-1.png)

```
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's inorder successor node is 2. Note that both p and the return value is of TreeNode type.
```

**Example 2:**

![tree-2](images/tree-2.png)

```
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no inorder successor of the current node, so the answer is null.
```

**Constraints:**

- All Nodes will have unique values.