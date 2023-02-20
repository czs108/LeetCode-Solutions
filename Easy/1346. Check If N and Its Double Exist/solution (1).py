# 1346. Check If N and Its Double Exist

# Runtime: 40 ms, faster than 98.82% of Python3 online submissions for Check If N and Its Double Exist.

# Memory Usage: 14.4 MB, less than 9.05% of Python3 online submissions for Check If N and Its Double Exist.


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        prev = set()
        for i, n in enumerate(arr):
            if n * 2 in prev or n * 0.5 in prev:
                return True
            if n not in prev:
                prev.add(n)
        return False