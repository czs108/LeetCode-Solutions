# 219. Contains Duplicate II

# Runtime: 104 ms, faster than 21.13% of Python3 online submissions for Contains Duplicate II.

# Memory Usage: 19.6 MB, less than 93.02% of Python3 online submissions for Contains Duplicate II.


class Solution:
    # Sliding Window
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        win = set()
        for i in range(len(nums)):
            if nums[i] in win:
                return True
            win.add(nums[i])
            if len(win) > k:
                win.remove(nums[i - k])
        return False