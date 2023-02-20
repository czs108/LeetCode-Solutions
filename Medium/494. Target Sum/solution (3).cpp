// 494. Target Sum


class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        nums_ = &nums;
        return calcSum(0, target);
    }

private:
    int calcSum(const int idx, const int remain) {
        if (idx == nums_->size()) {
            return remain == 0 ? 1 : 0;
        } else if (counts_[idx].count(remain)) {
            return counts_[idx][remain];
        } else {
            const auto num {nums_->at(idx)};
            const auto add {calcSum(idx + 1, remain + num)};
            const auto sub {calcSum(idx + 1, remain - num)};
            counts_[idx][remain] = add + sub;
            return counts_[idx][remain];
        }
    }

    vector<int>* nums_;
    unordered_map<int, unordered_map<int, int>> counts_;
};