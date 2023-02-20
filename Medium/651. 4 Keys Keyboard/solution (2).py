# 651. 4 Keys Keyboard

# Runtime: 32 ms, faster than 78.26% of Python3 online submissions for 4 Keys Keyboard.

# Memory Usage: 14.2 MB, less than 84.78% of Python3 online submissions for 4 Keys Keyboard.


class Solution:
    """
    The best sequence only has two patterns:
        1. A, A, ..., A, when `n` is small.
        2. A, A, ..., Ctrl + A, Ctrl + C, Ctrl + V, Ctrl + V, ..., Ctrl + A, Ctrl + C, Ctrl + V, Ctrl + V, when `n` is large.
    """
    def maxA(self, n: int) -> int:
        # max_count[i] means the maximum number of 'A' after pressing `i` keys.
        max_count = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            press_a = max_count[i - 1] + 1
            # `j` is the previous time finishing pressing Ctrl + A, Ctrl + C
            press_cv = 0
            for j in range(2, i):
                # Append (i -j + 1) times from the buffer.
                press_cv = max(press_cv, max_count[j - 2] * (i - j + 1))
            max_count[i] = max(press_a, press_cv)
        return max_count[-1]