# 225. Implement Stack using Queues

> Easy

------

Implement the following operations of a stack using queues.

- `push(x)` pushes element `x` onto stack.
- `pop()` removes the element on top of the stack.
- `top()` gets the top element.
- `empty()` returns whether the stack is empty.

**Example:**

```c++
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
```

You may assume that all operations are valid (for example, no `pop` or `top` operations will be called on an empty stack).