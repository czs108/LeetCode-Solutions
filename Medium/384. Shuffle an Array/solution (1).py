# 384. Shuffle an Array

# Runtime: 304 ms, faster than 80.62% of Python3 online submissions for Shuffle an Array.

# Memory Usage: 19.9 MB, less than 5.55% of Python3 online submissions for Shuffle an Array.


import random

class Solution:
    # Brute Force
    def __init__(self, nums: list[int]) -> None:
        self._origin: list[int] = list(nums)

    def reset(self) -> list[int]:
        return list(self._origin)

    def shuffle(self) -> list[int]:
        aux = list(self._origin)
        res = []
        for _ in range(len(self._origin)):
            remove_idx = random.randrange(len(aux))
            res.append(aux.pop(remove_idx))
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()