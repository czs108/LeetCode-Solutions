# 703. K-th Largest Element in a Stream

> Easy

------

Design a class to find the `k`-th largest element in a stream. Note that it is the `k`-th largest element in the sorted order, not the `k`-th distinct element.

Implement `KthLargest` class:

- `KthLargest(int k, int[] nums)` initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)` appends the integer `val` to the stream and returns the element representing the `k`-th largest element in the stream.

**Example:**

```
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output:
[null, 4, 5, 5, 8, 8]

Explanation:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

**Constraints:**

- It is guaranteed that there will be at least `k` elements in the array when you search for the `k`-th element.