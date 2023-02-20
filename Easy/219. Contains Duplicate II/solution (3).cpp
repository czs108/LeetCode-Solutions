// 219. Contains Duplicate II

// Runtime: 187 ms, faster than 94.37% of C++ online submissions for Contains Duplicate II.

// Memory Usage: 77.2 MB, less than 60.05% of C++ online submissions for Contains Duplicate II.


class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> seen;
        for (int i = 0; i != nums.size(); ++i) {
            if (auto found = seen.find(nums[i]); found != seen.end()) {
                if (i - found->second <= k) {
                    return true;
                }
            }

            seen[nums[i]] = i;
        }

        return false;
    }
};