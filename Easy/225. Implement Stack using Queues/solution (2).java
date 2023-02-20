// 225. Implement Stack using Queues


// Two Queues - Push O(n), Pop O(1)
class MyStack {

    private int top = 0;

    private Queue<Integer> mainQue = new LinkedList<>();
    private Queue<Integer> helperQue = new LinkedList<>();

    /** Initialize your data structure here. */
    public MyStack() { }

    /** Push element x onto stack. */
    public void push(int x) {
        helperQue.add(x);
        top = x;
        while (!mainQue.isEmpty()) {
            helperQue.add(mainQue.remove());
        }

        Queue<Integer> temp = mainQue;
        mainQue = helperQue;
        helperQue = temp;
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        int ret = mainQue.remove();
        if (!mainQue.isEmpty()) {
            top = mainQue.peek();
        }

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