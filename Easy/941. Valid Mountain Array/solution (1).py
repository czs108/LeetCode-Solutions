# 941. Valid Mountain Array

class Solution:
    # One Pass
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False

        i = 0
        # Walk up.
        while i + 1 != len(arr) and arr[i] < arr[i + 1]:
            i += 1

        # Peak can't be the first or last.
        if i == 0 or i == len(arr) - 1:
            return False

        # Walk down.
        while i + 1 != len(arr) and arr[i] > arr[i + 1]:
            i += 1

        return i == len(arr) - 1