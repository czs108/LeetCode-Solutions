# 346. Moving Average from Data Stream

> Easy

------

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the `MovingAverage` class:

- `MovingAverage(int size)` initializes the object with the size of the window `size`.
- `double next(int val)` returns the moving average of the last `size` values of the stream.

**Example:**

```
Input:
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output:
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation:
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1);      // return 1.0 = 1 / 1
movingAverage.next(10);     // return 5.5 = (1 + 10) / 2
movingAverage.next(3);      // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5);      // return 6.0 = (10 + 3 + 5) / 3
```