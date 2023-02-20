// 295. Find Median from Data Stream

// Runtime: 583 ms, faster than 8.20% of C++ online submissions for Find Median from Data Stream.

// Memory Usage: 116.9 MB, less than 98.73% of C++ online submissions for Find Median from Data Stream.


#include <queue>

class MedianFinder {
public:
    void addNum(int num) {
        // The max-heap is allowed to store, at worst, one more element more than the min-heap.
        low_.push(num);

        // Balancing step.
        high_.push(low_.top());
        low_.pop();

        if (low_.size() < high_.size()) {
            // Maintain size property.
            low_.push(high_.top());
            high_.pop();
        }
    }

    double findMedian() {
        return low_.size() > high_.size() ? low_.top() : (static_cast<double>(low_.top()) + high_.top()) / 2;
    }

private:
    // A max-heap to store the smaller half of the numbers.
    priority_queue<int> low_{};
    // A min-heap to store the larger half of the numbers.
    priority_queue<int, vector<int>, greater<int>> high_{};
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */