// 225. Implement Stack using Queues

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Implement Stack using Queues.

// Memory Usage: 38.5 MB, less than 6.67% of Java online submissions for Implement Stack using Queues.


// Two Queues - Push O(1), Pop O(n)
class MyStack {

    private int top = 0;

    private Queue<Integer> mainQue = new LinkedList<>();
    private Queue<Integer> helperQue = new LinkedList<>();

    /** Initialize your data structure here. */
    public MyStack() { }

    /** Push element x onto stack. */
    public void push(int x) {
        mainQue.add(x);
        top = x;
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        while (mainQue.size() > 1) {
            top = mainQue.remove();
            helperQue.add(top);
        }

        int ret = mainQue.remove();
        Queue<Integer> temp = mainQue;
        mainQue = helperQue;
        helperQue = temp;
        return ret;
    }

    /** Get the top element. */
    public int top() {
        return top;
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return mainQue.isEmpty();
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