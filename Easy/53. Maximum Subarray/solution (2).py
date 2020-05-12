# 53. Maximum Subarray

# 200 / 202 test cases passed.
# Status: Time Limit Exceeded


class Solution:
    # Divide and conquer
    def maxSubArray(self, nums: List[int]) -> int:
        return self.__maxSubArray(nums, 0, len(nums) - 1)

    def __maxSubArray(self, nums: List[int], left: int, right: int) -> int:
        if left >= right:
            return nums[left]
        else:
            mid = left + (right - left) // 2
            return max(self.__maxSubArray(nums, left, mid),
                self.__maxSubArray(nums, mid + 1, right),
                self.__maxCrossingSubArray(nums, left, mid, right))

    def __maxCrossingSubArray(self, nums: List[int], left: int, mid: int, right: int) -> int:
        curr_max_sum = nums[mid]
        left_max_sum = curr_max_sum
        for i in range(mid - 1, -1, -1):
            curr_max_sum = curr_max_sum + nums[i]
            left_max_sum = max(curr_max_sum, left_max_sum)

        curr_max_sum = nums[mid + 1]
        right_max_sum = curr_max_sum
        for i in range(mid + 2, len(nums)):
            curr_max_sum = curr_max_sum + nums[i]
            right_max_sum = max(curr_max_sum, right_max_sum)

        return left_max_sum + right_max_sum