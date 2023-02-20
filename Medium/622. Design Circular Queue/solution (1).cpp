// 622. Design Circular Queue


class MyCircularQueue {
public:
    MyCircularQueue(int k) {
        vals_.resize(k);
        capacity_ = k;
    }

    bool enQueue(int value) {
        if (!isFull()) {
            if (isEmpty()) {
                head_ = 0;
                tail_ = 0;
            } else {
                tail_ = (tail_ + 1) % capacity_;
            }

            vals_[tail_] = value;
            return true;
        } else {
            return false;
        }
    }

    bool deQueue() {
        if (!isEmpty()) {
            if (head_ == tail_) {
                head_ = -1;
                tail_ = -1;
            } else {
                head_ = (head_ + 1) % capacity_;
            }

            return true;
        } else {
            return false;
        }
    }

    int Front() const {
        if (!isEmpty()) {
            return vals_[head_];
        } else {
            return -1;
        }
    }

    int Rear() const {
        if (!isEmpty()) {
            return vals_[tail_];
        } else {
            return -1;
        }
    }

    bool isEmpty() const {
        return head_ == -1;
    }

    bool isFull() const {
        return ((tail_ + 1) % capacity_) == head_;
    }

private:
    int head_ {-1};
    int tail_ {-1};
    vector<int> vals_;
    int capacity_;
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */