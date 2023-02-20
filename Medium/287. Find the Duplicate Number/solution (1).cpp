// 287. Find the Duplicate Number


class Solution {
public:
    // Binary Search
    int findDuplicate(vector<int>& nums) {
        nums_ = &nums;
        size_t left {1}, right {nums.size()};
        int duplicate {0};
        while (left <= right) {
            auto mid {left + (right - left) / 2};
            if (smallOrEqual(mid) > mid) {
                duplicate = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return duplicate;
    }

private:
    size_t smallOrEqual(const int curr) const {
        size_t count {0};
        for (const auto n : *nums_) {
            if (n <= curr) {
                ++count;
            }
        }

        return count;
    }

    vector<int>* nums_;
};