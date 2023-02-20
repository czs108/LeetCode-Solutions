// 740. Delete and Earn


class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        initPoints(nums);
        vector<int> maxPoints(maxNum_ + 1);
        maxPoints[1] = getPoint(1);

        for (int i = 2; i < maxPoints.size(); i++) {
            maxPoints[i] =
                max(maxPoints[i - 1], maxPoints[i - 2] + getPoint(i));
        }

        return maxPoints.back();
    }

private:
    void initPoints(vector<int>& nums) {
        for (int n : nums) {
            points_[n] += n;
            maxNum_ = max(maxNum_, n);
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
    int maxNum_ = 0;
};