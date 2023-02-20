# 624. Maximum Distance in Arrays

# Runtime: 1612 ms, faster than 100.00% of Python3 online submissions for Maximum Distance in Arrays.

# Memory Usage: 41.1 MB, less than 27.78% of Python3 online submissions for Maximum Distance in Arrays.


import math

class Solution:
    # Single Scan
    def maxDistance(self, arrays: list[list[int]]) -> int:
        # Each tuple stores a value and its array index.
        largest, second_largest = (-math.inf, None), (-math.inf, None)
        smallest, second_smallest = (math.inf, None), (math.inf, None)

        for i in range(len(arrays)):
            array = arrays[i]

            # Update the largest and second largest values.
            if array[-1] > largest[0]:
                second_largest = largest
                largest = (array[-1], i)
            elif array[-1] > second_largest[0]:
                second_largest = (array[-1], i)

            # Update the smallest and second smallest values.
            if array[0] < smallest[0]:
                second_smallest = smallest
                smallest = (array[0], i)
            elif array[0] < second_smallest[0]:
                second_smallest = (array[0], i)

        # The largest and smallest values are not from the same array.
        if largest[1] != smallest[1]:
            return abs(largest[0] - smallest[0])
        else:
            return max(abs(largest[0] - second_smallest[0]), abs(second_largest[0] - smallest[0]))