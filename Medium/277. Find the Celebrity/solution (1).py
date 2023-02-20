# 277. Find the Celebrity

# Runtime: 1832 ms, faster than 77.50% of Python3 online submissions for Find the Celebrity.

# Memory Usage: 14.6 MB, less than 13.36% of Python3 online submissions for Find the Celebrity.


# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
class Solution:
    def findCelebrity(self, n: int) -> int:

        def is_celebrity(i: int) -> bool:
            for j in range(n):
                if i != j:
                    if knows(i, j) or not knows(j, i):
                        return False
            return True

        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        return candidate if is_celebrity(candidate) else -1