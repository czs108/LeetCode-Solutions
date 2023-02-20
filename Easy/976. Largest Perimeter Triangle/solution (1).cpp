// 976. Largest Perimeter Triangle

// Runtime: 38 ms, faster than 95.34% of C++ online submissions for Largest Perimeter Triangle.

// Memory Usage: 21.8 MB, less than 71.51% of C++ online submissions for Largest Perimeter Triangle.


class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = nums.size() - 3; i >= 0; --i) {
            if (nums[i] + nums[i + 1] > nums[i + 2]) {
                return nums[i] + nums[i + 1] + nums[i + 2];
            }
        }

        return 0;
    }
};