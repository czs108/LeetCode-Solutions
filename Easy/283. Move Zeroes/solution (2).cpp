// 283. Move Zeroes


class Solution {
public:
    // Two Pointers
    // Space Optimal, Operation Sub-Optimal
    void moveZeroes(vector<int>& nums) {

        auto last_non_zero{ 0 };

        // If the current element is not 0, then we need to
        // append it just in front of last non 0 element we found.
        for (auto i{ 0 }; i != nums.size(); i++) {
            if (nums[i] != 0) {
                nums[last_non_zero++] = nums[i];
            }
        }

        // After we have finished processing new elements,
        // all the non-zero elements are already at beginning of array.
        // We just need to fill remaining array with 0's.
        for (auto i{ last_non_zero }; i != nums.size(); i++) {
            nums[i] = 0;
        }
    }
};