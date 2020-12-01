// 225. Implement Stack using Queues

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Implement Stack using Queues.

// Memory Usage: 38.9 MB, less than 6.67% of Java online submissions for Implement Stack using Queues.


// One Queue - Push O(n), Pop O(1)
class MyStack {

    private LinkedList<Integer> que = new LinkedList<>();

    /** Initialize your data structure here. */
    public MyStack() { }

    /** Push element x onto stack. */
    public void push(int x) {
        que.add(x);
        int size = que.size();
        while (size > 1) {
            que.add(que.remove());
            size--;
        }
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return que.remove();
    }

    /** Get the top element. */
    public int top() {
        return que.peek();
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return que.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */