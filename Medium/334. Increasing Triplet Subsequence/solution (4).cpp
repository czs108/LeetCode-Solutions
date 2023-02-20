// 334. Increasing Triplet Subsequence

// Runtime: 143 ms, faster than 39.72% of C++ online submissions for Increasing Triplet Subsequence.

// Memory Usage: 61.4 MB, less than 87.63% of C++ online submissions for Increasing Triplet Subsequence.


class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if (nums.size() < 3) {
            return false;
        }

        int firstSmall = numeric_limits<int>::max();
        int secondSmall = numeric_limits<int>::max();
        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            if (num <= firstSmall) {
                firstSmall = num;
            } else if (num <= secondSmall) {
                secondSmall = num;
            } else {
                return true;
            }
        }

        return false;
    }
};