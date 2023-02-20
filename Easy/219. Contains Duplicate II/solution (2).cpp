// 219. Contains Duplicate II

// Runtime: 421 ms, faster than 32.94% of C++ online submissions for Contains Duplicate II.

// Memory Usage: 80.4 MB, less than 23.51% of C++ online submissions for Contains Duplicate II.


class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        set<int> seen;
        for (int i = 0; i != nums.size(); ++i) {
            if (seen.find(nums[i]) != seen.end()) {
                return true;
            }

            seen.insert(nums[i]);
            if (seen.size() > k) {
                seen.erase(nums[i - k]);
            }
        }

        return false;
    }
};