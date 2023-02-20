# 169. Majority Element

# Runtime: 316 ms, faster than 5.22% of Python3 online submissions for Majority Element.

# Memory Usage: 15.4 MB, less than 7.14% of Python3 online submissions for Majority Element.


class Solution:
    # Divide and Conquer
    def majorityElement(self, nums: list[int]) -> int:

        def majority_element(low: int, high: int) -> int:
            # Base case; the only element in an array of size 1 is the majority element.
            if low == high:
                return nums[low]

            # Recurse on left and right halves of this slice.
            mid = (high - low) // 2 + low
            left = majority_element(low, mid)
            right = majority_element(mid + 1, high)

            # If the two halves agree on the majority element, return it.
            if left == right:
                return left

            # Otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(low, high + 1) if nums[i] == left)
            right_count = sum(1 for i in range(low, high + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element(0, len(nums) - 1)