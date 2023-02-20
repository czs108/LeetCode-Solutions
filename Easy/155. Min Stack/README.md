# 155. Min Stack

> Easy

------

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time.

- `push(x)` pushes element `x` onto stack.
- `pop()` removes the element on top of the stack.
- `top()` gets the top element.
- `getMin()` retrieves the minimum element in the stack.

**Example:**

```
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Constraints:**

- Methods `pop`, `top` and `getMin` operations will always be called on non-empty stacks.