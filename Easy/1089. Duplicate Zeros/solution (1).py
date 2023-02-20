# 1089. Duplicate Zeros

# Runtime: 68 ms, faster than 69.18% of Python3 online submissions for Duplicate Zeros.


class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if len(arr) == 0:
            return arr

        possible_dups, last = self._zero_count(arr)
        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]

    def _zero_count(self, arr: list[int]) -> tuple[int, int]:
        # Find the number of zeros to be duplicated.
        possible_dups = 0
        last = 0
        for left in range(len(arr)):
            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list.
            if left >= len(arr) - possible_dups:
                last = len(arr) - 1 - possible_dups
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included.
                if left == len(arr) - 1 - possible_dups:
                    arr[-1] = 0
                    last = len(arr) - 2 - possible_dups
                    break
                possible_dups += 1
        return possible_dups, last