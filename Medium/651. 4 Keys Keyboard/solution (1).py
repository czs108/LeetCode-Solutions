# 651. 4 Keys Keyboard

# Time Limit Exceeded


class Solution:
    def maxA(self, n: int) -> int:
        max_count = {}

        # Get the maximum number of 'A' on the screen
        # when there are `screen` 'A's on the screen
        # and `copy` 'A's in the buffer currently, remaining `remain` presses.
        def get_max_count(remain: int, screen: int, copy: int) -> int:
            if remain <= 0:
                return screen
            elif (remain, screen, copy) not in max_count:
                press_a = get_max_count(remain - 1, screen + 1, copy)
                press_cv = get_max_count(remain - 1, screen + copy, copy)
                press_ca_cc = get_max_count(remain - 2, screen, screen)
                max_count[remain, screen, copy] = max(press_a, press_cv, press_ca_cc)
            return max_count[remain, screen, copy]

        return get_max_count(n, 0, 0)