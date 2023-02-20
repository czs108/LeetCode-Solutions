# 905. Sort Array By Parity


class Solution:
    # Sort
    # Use a custom comparator when sorting, to sort by parity.
    def sortArrayByParity(self, A: list[int]) -> list[int]:
        A.sort(key = lambda x: x % 2)
        return A