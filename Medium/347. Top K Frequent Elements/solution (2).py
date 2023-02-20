# 347. Top K Frequent Elements

# Runtime: 99 ms, faster than 79.31% of Python3 online submissions for Top K Frequent Elements.

# Memory Usage: 18.7 MB, less than 59.71% of Python3 online submissions for Top K Frequent Elements.


from collections import Counter
import random

class Solution:
    # Quickselect
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)
        unique = list(count.keys())

        def partition(left: int, right: int, pivot_idx: int) -> int:
            pivot_freq = count[unique[pivot_idx]]
            # 1. Move pivot to end.
            unique[pivot_idx], unique[right] = unique[right], unique[pivot_idx]

            # 2. Move all less frequent elements to the left.
            store_idx = left
            for i in range(left, right):
                if count[unique[i]] < pivot_freq:
                    unique[store_idx], unique[i] = unique[i], unique[store_idx]
                    store_idx += 1

            # 3. Move pivot to its final place.
            unique[right], unique[store_idx] = unique[store_idx], unique[right]

            return store_idx

        def quickselect(left: int, right: int, k_smallest: int) -> None:
            """
            Sort a list within left..right till k-th less frequent element takes its place.
            """
            if left == right:
                return

            # Select a random pivot index.
            pivot_idx = random.randint(left, right)

            # Find the pivot position in a sorted list.
            pivot_idx = partition(left, right, pivot_idx)

            # If the pivot is in its final sorted position.
            if k_smallest == pivot_idx:
                 return
            # Go left.
            elif k_smallest < pivot_idx:
                quickselect(left, pivot_idx - 1, k_smallest)
            # Go right.
            else:
                quickselect(pivot_idx + 1, right, k_smallest)

        n = len(unique)
        # k-th top frequent element is (n - k)-th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till (n - k)-th less frequent element takes its place (n - k) in a sorted array.
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements.
        return unique[n - k:]