# 401. Binary Watch

# Runtime: 32 ms, faster than 63.67% of Python3 online submissions for Binary Watch.

# Memory Usage: 14.1 MB, less than 41.96% of Python3 online submissions for Binary Watch.


class Solution:
    # Bit Counting
    def readBinaryWatch(self, num: int) -> list[str]:
        times = []
        hour_bits = { x: bin(x).count('1') for x in range(0, 12) }
        minute_bits = { x: bin(x).count('1') for x in range(0, 60) }
        for hour, hour_bit_cnt in hour_bits.items():
            for minute, minute_bit_cnt in minute_bits.items():
                if hour_bit_cnt + minute_bit_cnt == num:
                    times.append("{:d}:{:02d}".format(hour, minute))
        return times