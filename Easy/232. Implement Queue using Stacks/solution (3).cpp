// 232. Implement Queue using Stacks


class MyQueue {
public:
    MyQueue() {}

    void push(int x) {
        in_.push(x);
    }

    int pop() {
        if (out_.empty()) {
            inToOut();
        }

        const auto top {out_.top()};
        out_.pop();
        return top;
    }

    int peek() {
        if (out_.empty()) {
            inToOut();
        }

        return out_.top();
    }

    bool empty() {
        return in_.empty() && out_.empty();
    }

private:
    void inToOut() {
        while (!in_.empty()) {
            out_.push(in_.top());
            in_.pop();
        }
    }

    stack<int> in_;
    stack<int> out_;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */