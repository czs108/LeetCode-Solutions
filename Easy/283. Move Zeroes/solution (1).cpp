// 283. Move Zeroes

// Runtime: 8 ms, faster than 64.84% of C++ online submissions for Move Zeroes.

// Memory Usage: 9.6 MB, less than 7.03% of C++ online submissions for Move Zeroes.


class Solution {
public:
    // Space Sub-Optimal
    void moveZeroes(vector<int>& nums) {
        // Count the zeroes
        int zero_num{ 0 };
        for (auto i = 0; i != nums.size(); i++) {
            zero_num += (nums[i] == 0);
        }

        // Make all the non-zero elements retain their original order.
        vector<int> ans{};
        for (auto i = 0; i != nums.size(); i++) {
            if (nums[i] != 0) {
                ans.push_back(nums[i]);
            }
        }

        // Move all zeroes to the end.
        while (zero_num--) {
            ans.push_back(0);
        }

        // Combine the result
        for (auto i = 0; i != nums.size(); i++) {
            nums[i] = ans[i];
        }
    }
};