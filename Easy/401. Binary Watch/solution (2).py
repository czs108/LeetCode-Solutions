# 401. Binary Watch

# Runtime: 36 ms, faster than 26.41% of Python3 online submissions for Binary Watch.

# Memory Usage: 14 MB, less than 75.87% of Python3 online submissions for Binary Watch.


class Solution:
    _LED_NUM = 10
    _HOUR_LED_NUM = 4

    # Backtracking
    def __init__(self):
        self._times = []

    def readBinaryWatch(self, num: int):
        self._backtrack(num, 0, 0, 0)
        return self._times

    def _backtrack(self, num: int, pos: int, hour: int, minute: int):
        if hour > 11 or minute > 59:
            return
        elif num == 0:
            self._times.append("{:d}:{:02d}".format(hour, minute))
            return

        for i in range(pos, Solution._LED_NUM):
            if i < Solution._HOUR_LED_NUM:
                self._backtrack(num - 1, i + 1, hour + 2**i, minute)
            else:
                self._backtrack(num - 1, i + 1, hour, minute + 2**(i - Solution._HOUR_LED_NUM))