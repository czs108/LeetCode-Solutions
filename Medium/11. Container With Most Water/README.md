# 11. Container With Most Water

> Medium

------

Given `n` non-negative integers `a_1, a_2, ..., a_n` , where each represents a point at coordinate `(i, a_i)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, a_i)` and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

**Example 1:**

![container](images/container.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:**

```
Input: height = [1,1]
Output: 1
```

**Example 3:**

```
Input: height = [4,3,2,1,4]
Output: 16
```

**Example 4:**

```
Input: height = [1,2,1]
Output: 2
```