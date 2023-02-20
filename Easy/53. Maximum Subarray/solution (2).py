# 53. Maximum Subarray

# Runtime: 140 ms, faster than 5.27% of Python3 online submissions for Maximum Subarray.

# Memory Usage: 14.6 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.


class Solution:
    # Divide and Conquer
    def maxSubArray(self, nums: list[int]) -> int:

        def max_crossing_subarray(left: int, mid: int, right: int) -> int:
            curr_max_sum = nums[mid]
            left_max_sum = curr_max_sum
            for i in range(mid - 1, left - 1, -1):
                curr_max_sum = curr_max_sum + nums[i]
                left_max_sum = max(curr_max_sum, left_max_sum)

            curr_max_sum = nums[mid + 1]
            right_max_sum = curr_max_sum
            for i in range(mid + 2, right + 1):
                curr_max_sum = curr_max_sum + nums[i]
                right_max_sum = max(curr_max_sum, right_max_sum)

            return left_max_sum + right_max_sum

        def max_subarray(left: int, right: int) -> int:
            if left >= right:
                return nums[left]
            else:
                mid = left + (right - left) // 2
                return max(max_subarray(left, mid),
                            max_subarray(mid + 1, right),
                            max_crossing_subarray(left, mid, right))

        return max_subarray(0, len(nums) - 1)