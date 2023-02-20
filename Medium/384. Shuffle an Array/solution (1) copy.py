# 384. Shuffle an Array

# Runtime: 308 ms, faster than 77.87% of Python3 online submissions for Shuffle an Array.

# Memory Usage: 19.3 MB, less than 71.47% of Python3 online submissions for Shuffle an Array.


import random

class Solution:
    # Fisher-Yates Algorithm
    def __init__(self, nums: list[int]) -> None:
        self._origin: list[int] = list(nums)

    def reset(self) -> list[int]:
        return list(self._origin)

    def shuffle(self) -> list[int]:
        res = list(self._origin)
        for i in range(len(res)):
            swap_idx = random.randrange(i, len(res))
            res[i], res[swap_idx] = res[swap_idx], res[i]
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()