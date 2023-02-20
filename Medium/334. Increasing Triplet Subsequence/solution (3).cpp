// 334. Increasing Triplet Subsequence

// Time Limit Exceeded


class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if (nums.size() < 3) {
            return false;
        }

        vector<int> match(nums.size());
        fill(match.begin(), match.end(), 1);

        for (int i = 1; i < nums.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i]) {
                    match[i] = max(match[i], match[j] + 1);
                    if (match[i] >= 3) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
};