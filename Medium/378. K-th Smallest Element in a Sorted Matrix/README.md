# 378. Kth Smallest Element in a Sorted Matrix

> Medium

------

Given an `n × n` `matrix` where each of the rows and columns is sorted in ascending order, return the `k`-th smallest element in the `matrix`.

Note that it is the `k`-th smallest element in the sorted order, not the `k`-th distinct element.

You must find a solution with complexity better than `O(n^2)`.

**Example 1:**

```
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8-th smallest number is 13.
```

**Example 2:**

```
Input: matrix = [[-5]], k = 1
Output: -5
```