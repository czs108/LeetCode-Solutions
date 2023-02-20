# 487. Max Consecutive Ones II

# Runtime: 388 ms, faster than 37.74% of Python3 online submissions for Max Consecutive Ones II.

# Memory Usage: 14.4 MB, less than 27.64% of Python3 online submissions for Max Consecutive Ones II.


class Solution:
    # Linear Scan
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        curr_cnt_count = 0
        prev_cnt_count = 0
        for n in nums:
            curr_cnt_count += 1
            if n == 0:
                prev_cnt_count = curr_cnt_count
                curr_cnt_count = 0
            max_count = max(max_count, curr_cnt_count + prev_cnt_count)
        return max_count