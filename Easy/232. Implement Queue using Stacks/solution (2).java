// 232. Implement Queue using Stacks

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Implement Queue using Stacks.

// Memory Usage: 36.8 MB, less than 6.25% of Java online submissions for Implement Queue using Stacks.


// Two Stacks - Push O(1), Pop O(1)
class MyQueue {

    private int front = 0;

    private Stack<Integer> s1 = new Stack<>();
    private Stack<Integer> s2 = new Stack<>();

    /** Initialize your data structure here. */
    public MyQueue() { }

    /** Push element x to the back of queue. */
    public void push(int x) {
        if (s1.empty()) {
            front = x;
        }

        s1.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if (s2.isEmpty()) {
            while (!s1.isEmpty()) {
                s2.push(s1.pop());
            }
        }

        return s2.pop();
    }

    /** Get the front element. */
    public int peek() {
        if (!s2.isEmpty()) {
            return s2.peek();
        } else {
            return front;
        }
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return s1.isEmpty() && s2.isEmpty();
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