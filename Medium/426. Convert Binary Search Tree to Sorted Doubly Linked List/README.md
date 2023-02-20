# 426. Convert Binary Search Tree to Sorted Doubly Linked List

> Medium

------

Convert a binary search tree to a sorted circular doubly-linked list in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

**Example 1:**

![tree-1](images/tree-1.png)

```
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]
```

![list](images/list.png)

```
Explanation: The figure below shows the transformed binary search tree. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
```

![tree-2](images/tree-2.png)

**Example 2:**

```
Input: root = [2,1,3]
Output: [1,2,3]
```

**Example 3:**

```
Input: root = []
Output: []
Explanation: Input is an empty tree. Output is also an empty linked list.
```

**Example 4:**

```
Input: root = [1]
Output: [1]
```

Note that all the values of the tree are unique.