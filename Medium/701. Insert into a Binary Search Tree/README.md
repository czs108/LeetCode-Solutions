# 701. Insert into a Binary Search Tree

> Medium

------

You are given the `root` node of a Binary Search Tree (BST) and a `value` to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

**Example 1:**

![tree-1](images/tree-1.jpg)

```
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
```

Another accepted tree is:

![tree-2](images/tree-2.jpg)

**Example 2:**

```
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
```

**Example 3:**

```
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
```

**Constraints:**

- All the values `Node.val` are unique.