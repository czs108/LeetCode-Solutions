# 344. Reverse String


class Solution:
    # Recursion
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(left: int, right: int) -> None:
            if left < right:
                s[left], s[right] = s[right], s[left]
                swap(left + 1, right - 1)

        swap(0, len(s) - 1)