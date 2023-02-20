# 215. K-th Largest Element in an Array

# Runtime: 64 ms, faster than 79.19% of Python3 online submissions for K-th Largest Element in an Array.

# Memory Usage: 15.4 MB, less than 13.95% of Python3 online submissions for K-th Largest Element in an Array.


import random

class Solution:
    # Quickselect
    def findKthLargest(self, nums: list[int], k: int) -> int:

        def partition(left: int, right: int, pivot_idx: int) -> int:
            pivot = nums[pivot_idx]
            # 1. Move pivot to end.
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            # 2. Move all smaller elements to the left.
            store_idx = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1

            # 3. Move pivot to its final place.
            nums[right], nums[store_idx] = nums[store_idx], nums[right]

            return store_idx

        def select(left: int, right: int, k_smallest: int) -> int:
            """
            Returns the k-th smallest element of list within left..right.
            """
            if left == right:
                return nums[left]

            # Select a random pivot.
            pivot_idx = random.randint(left, right)

            # Find the pivot position in a sorted list.
            pivot_idx = partition(left, right, pivot_idx)

            # The pivot is in its final sorted position.
            if k_smallest == pivot_idx:
                 return nums[k_smallest]
            # Go left.
            elif k_smallest < pivot_idx:
                return select(left, pivot_idx - 1, k_smallest)
            # Go right.
            else:
                return select(pivot_idx + 1, right, k_smallest)

        # k-th largest is (n - k)-th smallest.
        return select(0, len(nums) - 1, len(nums) - k)