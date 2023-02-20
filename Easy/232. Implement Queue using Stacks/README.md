# 232. Implement Queue using Stacks

> Easy

------

Implement the following operations of a queue using stacks.

- `push(x)` pushes element `x` to the back of queue.
- `pop()` removes the element from in front of queue.
- `peek()` gets the front element.
- `empty()` returns whether the queue is empty.

**Example:**

```c++
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
```

You may assume that all operations are valid (for example, no `pop` or `peek` operations will be called on an empty queue).