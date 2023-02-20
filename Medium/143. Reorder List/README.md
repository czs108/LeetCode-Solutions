# 143. Reorder List

> Medium

------

You are given the head of a singly linked-list. The list can be represented as:

```
L(0) → L(1) → … → L(n - 1) → L(n)
```

Reorder the list to be on the following form:

```
L(0) → L(n) → L(1) → L(n - 1) → L(2) → L(n - 2) → …
```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

**Example 1:**

![list-1](images/list-1.jpg)

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

**Example 2:**

![list-2](images/list-2.jpg)

```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```