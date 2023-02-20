// 740. Delete and Earn

// Runtime: 51 ms, faster than 12.83% of C++ online submissions for Delete and Earn.

// Memory Usage: 13.1 MB, less than 60.14% of C++ online submissions for Delete and Earn.


class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        initPoints(nums);
        vector<int> maxPoints(uniqueNums_.size() + 1);
        maxPoints[1] = getPoint(uniqueNums_[0]);

        for (int i = 2; i < maxPoints.size(); i++) {
            if (uniqueNums_[i - 1] != uniqueNums_[i - 2] + 1) {
                maxPoints[i] = maxPoints[i - 1] + getPoint(uniqueNums_[i - 1]);
            } else {
                maxPoints[i] =
                    max(maxPoints[i - 1],
                        maxPoints[i - 2] + getPoint(uniqueNums_[i - 1]));
            }
        }

        return maxPoints.back();
    }

private:
    void initPoints(vector<int>& nums) {
        for (int n : nums) {
            points_[n] += n;
        }

        for (auto [n, _] : points_) {
            uniqueNums_.push_back(n);
        }
    }

    int getPoint(int num) const {
        if (auto point {points_.find(num)}; point != points_.end()) {
            return point->second;
        } else {
            return 0;
        }
    }

    map<int, int> points_;
    vector<int> uniqueNums_;
};