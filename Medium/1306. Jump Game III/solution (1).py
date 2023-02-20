# 1306. Jump Game III

# Runtime: 276 ms, faster than 98.60% of Python3 online submissions for Jump Game III.

# Memory Usage: 20.8 MB, less than 93.18% of Python3 online submissions for Jump Game III.


class Solution:
    # Breadth-First Search
    def canReach(self, arr: list[int], start: int) -> bool:
        que = [start]
        while que:
            idx = que.pop()
            if arr[idx] == 0:
                return True
            elif arr[idx] < 0:
                continue

            for next in [idx - arr[idx], idx + arr[idx]]:
                if 0 <= next < len(arr):
                    que.append(next)
            # Mark as visited.
            arr[idx] = -1
        return False