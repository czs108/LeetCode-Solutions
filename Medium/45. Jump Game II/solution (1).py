# 45. Jump Game II

# Runtime: 171 ms, faster than 49.95% of Python3 online submissions for Jump Game II.

# Memory Usage: 15.1 MB, less than 73.79% of Python3 online submissions for Jump Game II.


class Solution:
    # Greedy
    def jump(self, nums: list[int]) -> int:
            jmps = 0
            curr_jmp_end = 0
            farthest = 0
            for i in range(len(nums) - 1):
                # We continuously find the how far we can reach in the current jump.
                farthest = max(farthest, i + nums[i])
                # If we have come to the end of the current jump, we need to make another jump.
                if i == curr_jmp_end:
                    jmps += 1
                    curr_jmp_end = farthest
            return jmps