// 346. Moving Average from Data Stream


class MovingAverage {
public:
    MovingAverage(int size) {
        capacity_ = size;
    }

    double next(int val) {
        if (vals_.size() == capacity_) {
            const auto first {vals_.front()};
            vals_.pop();
            sum_ -= first;
        }

        sum_ += val;
        vals_.push(val);
        return (double)sum_ / vals_.size();
    }

    queue<int> vals_;
    int capacity_;
    int sum_ {0};
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */