// 283. Move Zeroes

// Runtime: 4 ms, faster than 97.98% of C++ online submissions for Move Zeroes.

// Memory Usage: 9.4 MB, less than 18.11% of C++ online submissions for Move Zeroes.


class Solution {
public:
    // Two Pointers
    // Optimal
    void moveZeroes(vector<int>& nums) {
        // All elements before the slow pointer `last_non_zero` are non-zeroes.
        // All elements between the current `i` and slow pointer are zeroes.
        for (auto last_non_zero{ 0 }, i{ 0 }; i != nums.size(); i++) {
            if (nums[i] != 0) {
                swap(nums[last_non_zero++], nums[i]);
            }
        }
    }
};