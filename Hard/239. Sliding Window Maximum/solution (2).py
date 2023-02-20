# 239. Sliding Window Maximum

# Runtime: 2552 ms, faster than 8.82% of Python3 online submissions for Sliding Window Maximum.

# Memory Usage: 30.8 MB, less than 14.24% of Python3 online submissions for Sliding Window Maximum.


class Solution:
    # Deque
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        win = MonotonicQueue()
        res = []
        for i in range(len(nums)):
            if i < k - 1:
                win.push(nums[i])
            else:
                win.push(nums[i])
                res.append(win.max())
                win.pop(nums[i - k + 1])
        return res


class MonotonicQueue:
    def __init__(self) -> None:
        self._que: list[int] = []

    def push(self, val: int):
        while self._que and self._que[-1] < val:
            self._que.pop()
        self._que.append(val)

    def max(self) -> int:
        return self._que[0]

    def pop(self, val: int) -> None:
        if self._que and self.max() == val:
            self._que.pop(0)