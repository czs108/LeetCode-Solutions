# 973. K Closest Points to Origin

# Runtime: 1028 ms, faster than 18.67% of Python3 online submissions for K Closest Points to Origin.

# Memory Usage: 19.9 MB, less than 66.37% of Python3 online submissions for K Closest Points to Origin.


import random

class Solution:
    # Quickselect
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        def dist(point: list[int]) -> int:
            return point[0]**2 + point[1]**2

        def partition(left: int, right: int, pivot_idx: int) -> int:
            pivot = points[pivot_idx]
            # 1. Move pivot to end.
            points[pivot_idx], points[right] = points[right], points[pivot_idx]

            # 2. Move all smaller elements to the left.
            store_idx = left
            for i in range(left, right):
                if dist(points[i]) < dist(pivot):
                    points[store_idx], points[i] = points[i], points[store_idx]
                    store_idx += 1

            # 3. Move pivot to its final place.
            points[right], points[store_idx] = points[store_idx], points[right]

            return store_idx

        def select(left: int, right: int, k_closest: int) -> int:
            if left == right:
                return left

            # Select a random pivot.
            pivot_idx = random.randint(left, right)

            # Find the pivot position in a sorted list.
            pivot_idx = partition(left, right, pivot_idx)

            # The pivot is in its final sorted position.
            if k_closest == pivot_idx:
                 return k_closest
            # Go left.
            elif k_closest < pivot_idx:
                return select(left, pivot_idx - 1, k_closest)
            # Go right.
            else:
                return select(pivot_idx + 1, right, k_closest)

        # Cannot use `select(0, len(points) - 1, k)`.
        return points[:select(0, len(points) - 1, k - 1) + 1]