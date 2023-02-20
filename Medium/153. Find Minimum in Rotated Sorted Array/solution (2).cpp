// 153. Find Minimum in Rotated Sorted Array


class Solution {
public:
    int findMin(vector<int>& nums) {
        size_t left {0}, right {nums.size() - 1};
        if (right == 0 || nums[right] > nums[0]) {
            return nums[0];
        }

        while (left < right) {
            auto mid {left + (right - left) / 2};
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return nums[left];
    }
};