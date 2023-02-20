# 658. Find K Closest Elements


class Solution:
    # Sort With Custom Comparator
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        sorted_arr = sorted(arr, key=lambda n: abs(x - n))
        return sorted([sorted_arr[i] for i in range(k)])