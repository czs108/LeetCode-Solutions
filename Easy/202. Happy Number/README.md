# 202. Happy Number

> Easy

------

Write an algorithm to determine if a number *n* is "*happy*".

A *happy* number is a number defined by the following process:

- Start with any *positive* integer, replace the number by the *sum* of the *squares* of its digits.
- Repeat the process until the number equals **1** (where it will stay), or it loops endlessly in a cycle which does not include **1**.

Those numbers for which this process ends in **1** are *happy* numbers.

Return `true` if *n* is a happy number, and `false` if not.

**Example:**

```
Input: 19
Output: true
```

Explanation:

1<sup>2</sup> + 9<sup>2</sup> = 82

8<sup>2</sup> + 2<sup>2</sup> = 68

6<sup>2</sup> + 8<sup>2</sup> = 100

1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1