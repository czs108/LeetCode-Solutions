// 703. K-th Largest Element in a Stream


class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) {
        maxSize_ = k;
        for (int num : nums) {
            push(num);
        }
    }

    int add(int val) {
        push(val);
        return vals_.top();
    }

private:
    void push(int val) {
        if (vals_.size() < maxSize_) {
            vals_.push(val);

        } else if (vals_.top() < val) {
            vals_.pop();
            vals_.push(val);
        }
    }

    int maxSize_;

    // Use a min-heap to store only top `k` entries.
    // The top of the heap will be the `k`-th largest.
    priority_queue<int, vector<int>, greater<int>> vals_;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */