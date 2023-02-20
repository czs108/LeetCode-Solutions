// 209. Minimum Size Subarray Sum

// Runtime: 20 ms, faster than 12.12% of C++ online submissions for Minimum Size Subarray Sum.

// Memory Usage: 10.7 MB, less than 8.09% of C++ online submissions for Minimum Size Subarray Sum.


class Solution {
public:
    // Binary Search
    int minSubArrayLen(int target, vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        vector<int> sums(nums.size() + 1, 0);
        for (auto i = 1; i <= nums.size(); ++i) {
            sums[i] = sums[i - 1] + nums[i - 1];
        }

        int ans = nums.size() + 1;
        for (auto i = 1; i <= nums.size(); ++i) {
            int to_find = target + sums[i - 1];
            auto bound = lower_bound(sums.begin(), sums.end(), to_find);
            if (bound != sums.end()) {
                ans = min(ans, static_cast<int>(bound - (sums.begin() + i - 1)));
            }
        }

        return ans <= nums.size() ? ans : 0;
    }
};