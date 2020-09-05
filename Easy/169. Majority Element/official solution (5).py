# 169. Majority Element

# Runtime: 316 ms, faster than 5.22% of Python3 online submissions for Majority Element.

# Memory Usage: 15.4 MB, less than 7.14% of Python3 online submissions for Majority Element.


class Solution:
    # Divide and Conquer
    def majorityElement(self, nums: List[int]) -> int:
        return Solution._majorityElementRec(nums, 0, len(nums) - 1)

    @staticmethod
    def _majorityElementRec(nums: List[int], low: int, high: int) -> int:
        # base case; the only element in an array of size 1 is the majority
        # element.
        if low == high:
            return nums[low]

        # recurse on left and right halves of this slice.
        mid = (high - low) // 2 + low
        left = Solution._majorityElementRec(nums, low, mid)
        right = Solution._majorityElementRec(nums, mid + 1, high)

        # if the two halves agree on the majority element, return it.
        if left == right:
            return left

        # otherwise, count each element and return the "winner".
        left_count = sum(1 for i in range(low, high + 1) if nums[i] == left)
        right_count = sum(1 for i in range(low, high + 1) if nums[i] == right)

        return left if left_count > right_count else right