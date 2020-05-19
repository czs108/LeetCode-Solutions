// 232. Implement Queue using Stacks

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Implement Queue using Stacks.

// Memory Usage: 37.2 MB, less than 6.25% of Java online submissions for Implement Queue using Stacks.


// Two Stacks - Push O(n), Pop O(1)
class MyQueue {

    private int front = 0;

    private Stack<Integer> mainStack = new Stack<>();
    private Stack<Integer> helperStack = new Stack<>();

    /** Initialize your data structure here. */
    public MyQueue() { }

    /** Push element x to the back of queue. */
    public void push(int x) {
        if (mainStack.empty()) {
            front = x;
        }

        // Reverse arrival order of the elements.
        while (!mainStack.isEmpty()) {
            helperStack.push(mainStack.pop());
        }

        helperStack.push(x);

        while (!helperStack.isEmpty()) {
            mainStack.push(helperStack.pop());
        }
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        int ret = mainStack.pop();
        if (!mainStack.empty()) {
            front = mainStack.peek();
        }

        return ret;
    }

    /** Get the front element. */
    public int peek() {
        return front;
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return mainStack.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */