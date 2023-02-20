# 912. Sort an Array

# Runtime: 688 ms, faster than 71.49% of Python3 online submissions for Sort an Array.

# Memory Usage: 25.2 MB, less than 12.82% of Python3 online submissions for Sort an Array.


class Solution:
    # Quick Sort
    def sortArray(self, nums: list[int]) -> list[int]:
        def partition(left: int, right: int) -> int:
            if left >= right:
                return left

            pivot_idx = left + (right - left) // 2
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            store_idx = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1
            nums[store_idx], nums[right] = nums[right], nums[store_idx]
            return store_idx

        def quick_sort(left: int, right: int) -> None:
            if left < right:
                pivot = partition(left, right)
                quick_sort(left, pivot - 1)
                quick_sort(pivot + 1, right)

        quick_sort(0, len(nums) - 1)
        return nums