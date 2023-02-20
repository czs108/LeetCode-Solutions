# 27. Remove Element

> Easy

------

Given an array `nums` and a value `val`, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with `O(1)` extra memory.

**Example 1:**

```
Input: nums = [3,2,2,3], val = 3
Output: 2
Explanation: The first two elements of nums are 2.
```

**Example 2:**

```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5
Explanation: The first five elements of nums are [0,1,3,0,4].
```

**Clarification:**

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

```c
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```