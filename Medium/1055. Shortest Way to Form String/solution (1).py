# 1055. Shortest Way to Form String

# Runtime: 74 ms, faster than 26.28% of Python3 online submissions for Shortest Way to Form String.

# Memory Usage: 14.2 MB, less than 86.78% of Python3 online submissions for Shortest Way to Form String.


class Solution:
    # Two Pointers | Greedy
    def shortestWay(self, source: str, target: str) -> int:
        for c in set(target):
            if c not in set(source):
                return -1

        i, j = 0, 0
        ans = 0
        while j < len(target):
            i = 0
            while i < len(source) and j < len(target):
                if source[i] == target[j]:
                    i += 1
                    j += 1
                else:
                    # Delete one letter from the source.
                    i += 1
            ans += 1
        return ans